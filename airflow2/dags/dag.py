"""Demo DAG for tweet extraction"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.models import Variable
from datetime import datetime
from airflow.utils.dates import days_ago
from tweets import get_write_tweets
import os


params = {
    'access_token': Variable.get("access_token"),
    'access_token_secret': Variable.get("access_token_secret"),
    'consumer_key': Variable.get("consumer_key"),
    'consumer_secret': Variable.get("consumer_secret"),
    'project_id': Variable.get("project_id")
    }


args = {
    'owner': 'Paulina Trejo',
    'email': 'paulinahtrejo@gmail.com',
    'retries': 3,
    'depends_on_past': True,
}


dag = DAG(
    dag_id='extraction',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    tags=['bash', 'python', 'tweet', 'extraction'],
    max_active_runs=1
)


task1 = BashOperator(
    dag=dag,
    task_id='task1',
    bash_command='pip install tweepy'
)

task2 = PythonOperator(
    dag=dag,
    task_id = 'task2',
    provide_context=True,
    python_callable=get_write_tweets,
    op_kwargs={'access_token': params['access_token'], 'access_token_secret': params['access_token_secret'],
    'consumer_key': params['consumer_key'],'consumer_secret': params['consumer_secret'],
    'project_id': params['project_id'],
    'database': 'tweets',
    'table': 'JetBlue',
    'search': 'JetBlue'
    }
)

task3 = PythonOperator(
    dag=dag,
    task_id = 'task3',
    provide_context=True,
    python_callable=get_write_tweets,
    op_kwargs={'access_token': params['access_token'], 'access_token_secret': params['access_token_secret'],
    'consumer_key': params['consumer_key'],'consumer_secret': params['consumer_secret'],
    'project_id': params['project_id'],
    'database':'tweets',
    'table': 'SouthwestAir',
    'search': 'SouthwestAir'
    }
)


task1 >> [task2,task3]
