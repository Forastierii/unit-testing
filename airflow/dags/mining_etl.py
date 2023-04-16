#import sys
#import os
#path = os.path.abspath(r"C:\Users\pfaprado\Documents\GitHub\unit-testing")
#sys.path.append(path)
#import data_processing


# Defining the process that will take place with our input data
def process(file):
    
    import pandas as pd
    
    file = pd.read_csv(file)
    print("Data was imported.")
    
    file = file[(file['output']=='Alumina')&(file['facility_type']=='Refinery')&(file['input']=='Nepheline ore, Limestone')]
    print("Data was filtered.")
    
    file = file.dropna(axis=1)
    print("Dropping empty columns.")
    
    file = file[['id', 'year', 'output_value_tonnes']]
    print("Year and production was selected for the output file.")
    
    ton_to_tonne_ratio = 1.1
    file['output_value_tonnes'] = file['output_value_tonnes'].values*ton_to_tonne_ratio
    print("Converting processing output from tonne to ton.")
    
    file.to_csv("/opt/airflow/data/processing_deliverable.csv", encoding='latin-1')
    print("Creating output file.")
    
    return

# Importing the necessary libraries to instantiate objects with DAG and Python Operator classes
from airflow.models import DAG
from airflow.operators.python import PythonOperator

# Setting the default args for the dag
default_args = {
    'owner':'Pedro Prado',
    'start_date': '2023-04-15',
    'end_date': '2023-04-16'
    'schedule_interval': '30 12 * * 3',
    'email_on_failure': False,
    'email_on_retry': False
}

# Creating a dag
dag = DAG(
    dag_id = 'processing_dag',
    default_args = default_args,
    catchup = False
)

# Creating our first operator, a Python Operator
processing_task = PythonOperator(
    task_id = 'processing_task',
    python_callable = process,
    op_kwargs = {'file':"/opt/airflow/data/processing.csv"},
    dag = dag
)