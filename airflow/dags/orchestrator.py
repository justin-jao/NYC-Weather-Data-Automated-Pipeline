import sys
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator # type: ignore
from docker.types import Mount # type: ignore
from datetime import datetime, timedelta    

sys.path.append('/opt/airflow/api-requests')
from insert_records import main # type: ignore

default_args = {
    'description': 'A DAG to orchestrate weather data fetching and insertion into the database',
    'start_date': datetime(2026, 8, 30),
    'catchup': False,
}

dag = DAG(
    dag_id="weather-api-dbt-orchestrator",
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id = 'ingest_data_task',
        python_callable = main  
    )

    task2 = DockerOperator(
            task_id='transform_data_task',
            image = 'ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
            command = 'run',
            working_dir = '/usr/app',
            mounts = [
                Mount(source='/home/justin/repos/weather-project-folder/dbt/my_project',
                      target = '/usr/app',
                      type = 'bind'),
                Mount(source='/home/justin/repos/weather-project-folder/dbt/profiles.yml',
                      target = '/root/.dbt/profiles.yml',
                      type = 'bind'),
            ],
            network_mode = 'weather-project-folder_my_network',
            docker_url = 'unix://var/run/docker.sock',
            auto_remove = 'success'
    )

    task1 >> task2
