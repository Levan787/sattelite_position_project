from airflow.models import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta
from open_csv import write_to_csv
from configs.constants import *
from json_data import merge_dictionary, get_dictionary_from_json
from psql_connector.PSQLDriver import PsqlDriver

default_args = {
    'owner': 'Levan',
    'retries': 5,
    'retry_delay': timedelta(seconds=5),
    'start_date': datetime(2022, 11, 20),
    'description': 'satellite_data_dag'
}


def take_json_data(ti):
    json_data = get_dictionary_from_json()
    ti.xcom_push(key='json_data', value=json_data)
    return json_data


def processing_json_data(ti):
    processing_iss_data = merge_dictionary()
    ti.xcom_push(key='processed_data', value=processing_iss_data)
    return processing_iss_data


def upload_json_data(ti):
    column_names = [SATELLITE_LONGITUDE, SATELLITE_LATITUDE, NEAREST_COUNTRY_NAME]
    satellite_data = merge_dictionary()
    # processed_data = ti.xcom_pull(key='processed_data')

    write_to_csv(CSV_FILE, satellite_data)
    # ti.xcom_push(key="upload_data", value=upload_data)
    # sql = PsqlDriver()
    #
    # sql.execute(sql.create_table(TABLE_NAME))
    # sql.execute(sql.insert_row(TABLE_NAME, column_names, satellite_data))

    return 'levan'


with DAG('parallel_dag', default_args=default_args,
         schedule_interval=timedelta(minutes=5)) as dag:
    task_1 = PythonOperator(
        task_id='taking_data',
        python_callable=take_json_data
    )
    task_2 = PythonOperator(
        task_id='processing_data',
        python_callable=processing_json_data

    )
    task_3 = PythonOperator(
        task_id='upload_data',
        python_callable=upload_json_data
    )

    task_1 >> task_2 >> task_3
