# APACHE AIRFLOW DAGS

**This is a repor for my apache airflow tests**

## Bigquery

**Notes:**<br>

1. Enable Bigquery API for the Project
2. Set Billing for the project
3. Create Service Account
4. Assign permissions for the account of step 3 (BigQuery Job User, BigQuery User, BigQuery Data Editor, Editor for the project)
5. In BigQuery page, create a dataset and set the location (Data location) to the same as where the queries will be run (eg. US). This is the case where the results of the query will be stored in a table
6. IMPORTANT: AIRFLOW_VERSION=2.0.1
   PYTHON_VERSION=3.8
   CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-\${AIRFLOW_VERSION}/constraints-\${PYTHON_VERSION}.txt"
   pip install "apache-airflow[gcp]==\${AIRFLOW_VERSION}" --constraint "\${CONSTRAINT_URL}"
7. Useful resource: https://medium.com/apache-airflow/a-simple-guide-to-start-using-apache-airflow-2-on-google-cloud-1811c2127445
