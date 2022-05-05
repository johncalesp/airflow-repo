from datetime import timedelta, datetime
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

dag_args = {
    'owner': '<InsertName>',
    'depends_on_past': False,
    'start_date': datetime(2022, 5, 3),
    'email': ['<InsertEmail>'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=3)}

dag = DAG(
    dag_id='bq_connection_google',
    start_date=datetime(2022, 5, 3),
    default_args=dag_args,
    end_date=None,
    schedule_interval='0 * * * *')

task_custom = BigQueryInsertJobOperator(
    task_id='task_custom_connection',
    configuration={
        "query": {
            "query": """
                SELECT subscriber_type FROM bigquery-public-data.austin_bikeshare.bikeshare_trips LIMIT 1000
            """,
            'destinationTable': {
                'projectId': '<Insert ProjectID>',
                'datasetId': '<Insert DatasetName>',
                'tableId': '<Insert Table Name>'
            },
            "useLegacySql": False,
            'allowLargeResults': True,
            'createDisposition':'CREATE_IF_NEEDED',
            'writeDisposition':'WRITE_TRUNCATE'
        }
    },
    dag=dag
)

task_custom