"""Demo DAG for tweet extraction"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.models import Variable
from datetime import datetime
from airflow.utils.dates import days_ago
from tweets import *
import os

path = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(path, 'train_set.py')
script_path2 = os.path.join(path, 'train_set_predictions.py')

params = {
    'bearer': Variable.get("bearer"),
    'project_id': Variable.get("project_id"),
    'script': script_path,
    'script2': script_path2    }


args = {
    'owner': 'Paulina Trejo',
    'email': 'paulinahtr@gmail.com',
    'retries': 3,
    'depends_on_past': True,
}


dag = DAG(
    dag_id='extraction',
    default_args=args,
    schedule_interval='*/2 * * * *',
    start_date=days_ago(2),
    tags=['bash', 'python', 'tweet', 'extraction'],
    max_active_runs=1
)


task1 = BashOperator(
    dag=dag,
    params=params,
    task_id='task1',
    bash_command='python3 {{ params.script }}'
)



task2 = PythonOperator(
    dag=dag,
    task_id = 'task2',
    provide_context=True,
    python_callable=get_write_tweets,
    op_kwargs={'bearer': params['bearer'],'project_id': params['project_id'],
    'database': 'tweets_extraction',
    'table': 'JetBlue',
    'search': 'JetBlue'
    }
)

task3= PythonOperator(
    dag=dag,
    task_id = 'task3',
    provide_context=True,
    python_callable=get_write_tweets,
    op_kwargs={'bearer': params['bearer'],'project_id': params['project_id'],
    'database':'tweets_extraction',
    'table': 'SouthwestAir',
    'search': 'SouthwestAir'
    }
)


update = """
CREATE OR REPLACE TABLE train.train_set_predictions AS
WITH new_tweets AS (
SELECT DISTINCT *, null as label
FROM(
SELECT DISTINCT tweet_id as id,text, 'jb' AS company
FROM `tweets_extraction.JetBlue` 
WHERE RAND() < 50/100
union all (SELECT DISTINCT tweet_id as id,text, 'sw' AS company
FROM `tweets_extraction.SouthwestAir` 
WHERE RAND() < 50/100)
)
WHERE id not in (select distinct safe_cast(id as int64) as id from `train.train_set` ))
SELECT safe_cast(id as int64) as id,text,company,safe_cast(label as int64) as label
FROM `train.train_set` 
UNION ALL (select * from new_tweets)
ORDER BY id
"""

task4= BigQueryOperator(
    task_id = 'task4',
    dag=dag,
    sql=update,
    use_legacy_sql=False,
    bigquery_conn_id="google_cloud_default"
    )


task5 = BashOperator(
    dag=dag,
    params=params,
    task_id='task5',
    bash_command='python3 {{ params.script2 }}'
)



task1 >> [task2,task3] >> task4 >> task5