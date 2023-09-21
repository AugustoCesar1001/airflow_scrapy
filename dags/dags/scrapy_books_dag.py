from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.models import Variable
from datetime import datetime, timedelta


# Configurações para inicialização da DAG //// scrapy crawl bookspider -O cleandata.json
default_args = {
    "owner": "Augusto",
    "description": "Crawler using Scrapy",
    "depends_on_past": False,
    "start_date": datetime(2023, 9, 17),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

# /opt/airflow/project_a
bookspider_scraper_path = "/opt/airflow/project_a"
bookspider_data = "/opt/airflow/data/"


with DAG("bookspider_airflow", default_args=default_args, catchup=False) as dag:

    t1 = BashOperator(
        task_id = "cat_books",
        bash_command="cd {} && scrapy crawl bookspider -O {}cleandata.json".format(bookspider_scraper_path, bookspider_data),
        dag = dag
    )

    t2 = BashOperator(
        task_id="storing",
        bash_command="exit 0"
    )

    t1 >> t2
