# airflow_tutorial

Setup Python

    install python 3.7.x or above, download here

    Follow the installation steps, and make sure python 3 is successfully installed in your machine :

    python --version

    go to the repository directory and create a virtual environment :

    python -m venv venv

    Activate the virtual environment

    source venv/bin/activate (Linux/MacOS)

    venv\Scripts\activate (Windows)

Install Python IDE

You can use your favorite IDE :

    PyCharm
    Visual Code
    Spyder
    Vim
    etc

Setup MyQSL Database :

In this workshop we will use MySQL 5.7 or above. There are two options to install the database server :

Options 1 : Local server or VM :

    Download the installation package :
        Windows : Download
        Linux : Download
        MacOS : Download
    Double click teh installer and follow the installation instruction

Options 2 : Install with Docker :

    docker pull mysql:5.7
    docker run --publish=3306:3306 --name local-mysql -e MYSQL_ROOT_PASSWORD=password123 -d mysql:5.7

Install MySQL Workbench (or your favorite MySQL Client) :

    Download the installer : Download
    Double click the installer and follow the instruction.

PySpark

    Install PySpark => pip install pyspark or python -m pip install pyspark

Great Expectations

    Install Great Expectations : pip install great_expectations or python -m pip install great_expectations

Airflow

Install Airflow on Linux / MacOS :

export AIRFLOW_HOME=~/airflow
AIRFLOW_VERSION=2.1.0
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

Install Airflow on Windows:

The recommended way to install Airflow on Windows machine is by enabling Windows subsystem for Linux (WSL), you can follow this tutorial : Install Airflow on Windows using WSL

If you cannot enable WSL in your machine for some reasons, you can try to install it directly as follows :

export AIRFLOW_HOME=C:\airflow
AIRFLOW_VERSION=2.1.0
PYTHON_VERSION=3.8 (Change it with your python version)
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
python -m pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

Initialize the Airflow database

Disable Airflow example dags loading (Optional):

    Go to Airflow home directory : cd $AIRFLOW_HOME (Linux/MacOS) or dir %AIRFLOW_HOME% (Windows)

    Edit airflow.cfg , and make this change :

    load_examples = True

    Change to

    load_examples = False

Initiate the database :

airflow db init

Create Airflow user

airflow users create \
    --username admin \
    --firstname admin \
    --lastname idbigdata \
    --role Admin \
    --email admin@admin.com

Start Airflow services

start the web server, default port is 8080

airflow webserver --port 8080

start the scheduler open a new terminal or else run webserver with -D option to run it as a daemon

airflow scheduler

Now, you can open browser and access : http://localhost:8080
