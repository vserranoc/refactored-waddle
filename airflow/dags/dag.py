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


params = {
    'bearer': Variable.get("bearer"),
    'project_id': Variable.get("project_id")    }


args = {
    'owner': 'Paulina Trejo',
    'email': 'paulinahtrejo@gmail.com',
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


task1 = PythonOperator(
    dag=dag,
    task_id = 'task1',
    provide_context=True,
    python_callable=get_write_tweets,
    op_kwargs={'bearer': params['bearer'],'project_id': params['project_id'],
    'database': 'tweets_extraction',
    'table': 'JetBlue',
    'search': 'JetBlue'
    }
)

task2= PythonOperator(
    dag=dag,
    task_id = 'task2',
    provide_context=True,
    python_callable=get_write_tweets,
    op_kwargs={'bearer': params['bearer'],'project_id': params['project_id'],
    'database':'tweets_extraction',
    'table': 'SouthwestAir',
    'search': 'SouthwestAir'
    }
)


task1
task2