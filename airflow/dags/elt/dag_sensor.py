"""DAG Model"""

from airflow import DAG
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
from dags.modelling import modelling
from dags.train_set_predictions import train_set_predictions
from datetime import datetime
import os

args = {
    'owner': 'Luis Valdez ',
    'email': 'luigi1089@gmail.com',
    'retries': 2,
    'depends_on_past': True,
}
path = os.path.dirname(os.path.abspath(__file__))
script = os.path.join(path, 'modelling')
script_2 = os.path.join(path, 'train_set_predictions.py')

params = {
    'bucket': Variable.get("bucket"),
    'folder': 'dags/',
    'project_id': Variable.get("project_id"),
    'script' : script,
    'script2' : script_2
}

dag = DAG(
    dag_id='model_dag',
    default_args=args,
    schedule_interval='*/2 * * * *',
    start_date=days_ago(2),
    catchup=True,
    max_active_runs=1
)

# Task 1: External Task Sensor
task1 = ExternalTaskSensor(
    dag = dag,
    task_id = 'extract_task_sensor',
    external_dag_id = 'dags_dag',
    external_task_id = 'task5'
)
# Task 2: Run Model
task2 = BashOperator(
    dag=dag,
    params=params,
    task_id='task2',
    bash_command='python3 {{ params.script }}'
)

task3 = PythonOperator(
    dag = dag,
    params = params,
    task_id = 'task3',
    provide_context = True,
    python_callable = modelling,
    op_kwargs = {'vms-2022': params['vms-2022'],'path': params['dags/'],
    }
)

# Task 4: Generate Score
task4 = BigQueryOperator(
    dag = dag,
    params = params,
    task_id = 'task4',
    use_legacy_sql = False,
    bigquery_id = 'score_bq'
)

task1 >> task2 >> task3 >> task4
