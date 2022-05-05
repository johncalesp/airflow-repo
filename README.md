# APACHE AIRFLOW DAGS

**This is a repor for my apache airflow tests**

## Bigquery

**Notes:**<br>

1. Enable Bigquery API for the Project
2. Set Billing for the project
3. Create Service Account
4. Assign permissions for the account of step 3 (BigQuery Job User, BigQuery User, BigQuery Data Editor, Editor for the project)
5. In BigQuery page, create a dataset and set the location (Data location) to the same as where the queries will be run (eg. US). This is the case where the results of the query will be stored in a table
