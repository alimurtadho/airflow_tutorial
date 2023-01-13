import pendulum
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

today = "{{ ds }}"

def satu(x):
    namaFile = f"{x}_namaFile.csv"
    print(namaFile)

def dags(dag):
    print(dag)

default_args = {
    'owner' : 'ali',
    'retries' : 1,
    'retry_delay' : timedelta(minutes=3)
}

with DAG(
    dag_id = 'testing_2',
    default_args = default_args,
    start_date = pendulum.datetime(2022, 9, 19, tz="Asia/Jakarta"),
    schedule_interval='@once',
    catchup=False,
    tags = ["testing"]
) as dag:
    start_task = DummyOperator(
        task_id = "start"
    )

    bash1 = BashOperator(
        task_id = "bash1",
        bash_command = "pwd"  #"echo {{ ds_nodash }}"
    )

    bash2 = BashOperator(
        task_id = "bash2",
        bash_command = "ls -lh"  #"echo {{ ds_nodash }}"
    )

    sat = PythonOperator(
        task_id = "satu",
        python_callable = satu,
        op_kwargs = {
            "x" : "{{ ds_nodash }}"
        },
        do_xcom_push = False
    )

    dua = PythonOperator(
        task_id = "cek_ds",
        python_callable = dags,
        op_kwargs = {
            "dag" : "{{ ti.execution_date + macros.timedelta(hours = 7) }}"
        },
        do_xcom_push = False
    )

    end_task = DummyOperator(
        task_id = "end"
    )

    start_task >> bash1 >> bash2 >> sat >> dua >> end_task 