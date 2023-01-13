# Import libraries as much as needed
import pendulum
import pandas as pd
from airflow import DAG
# from utils.utils import sqlcol
from datetime import datetime, timedelta
from airflow.utils.task_group import TaskGroup
from airflow.operators.python import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.postgres_operator import PostgresOperator

# Write down your code. If you have long and complex query code, 
# please keep in mind to separate it into other script and store it in folder sql,
# then call it here
# Don't forget to add 'data_ingestion_time'/'data_updated_at' column
def get_data_load():
    src = PostgresHook(postgres_conn_id='conection')
    dest = PostgresHook(postgres_conn_id='conection')
    dest_engine = dest.get_sqlalchemy_engine()
    src_conn = src.get_conn()
    scr_cursor = src_conn.cursor()

    get_sql = '''SELECT * FROM public.levels'''
    scr_cursor.execute(get_sql)
    rows = scr_cursor.fetchall()
    col_names = []
    for names in scr_cursor.description:
        col_names.append(names[0])
    new = pd.DataFrame(rows, columns=col_names)
    outputdict = sqlcol(new)
    new["data_updated_at"] = pendulum.now()

    new.to_sql(
        'binar_core_levels1',
        dest_engine, 
        if_exists='append', 
        index=False, 
        schema='dl',
        dtype= outputdict)
    src_conn.close()
    print('success')

# Define function to call task group, consist of all tasks that we want to run in our DAG. 
# This function will imported on main script .py. Even if you only have one task, don't forget to define on task group. 
def core_levels_group(dag: DAG) -> TaskGroup:
    with TaskGroup("core_levels_group") as extract_group:
        create_table = PostgresOperator(      
                task_id = "create_table_task",
                postgres_conn_id = "conection",
                sql = 'utils/sql/test_sql.sql',
                dag = dag
                )
    
        get_update_load_data = PythonOperator(
                task_id = 'get_update_load',
                python_callable = get_data_load,
                )

    create_table >> get_update_load_data

    return extract_group