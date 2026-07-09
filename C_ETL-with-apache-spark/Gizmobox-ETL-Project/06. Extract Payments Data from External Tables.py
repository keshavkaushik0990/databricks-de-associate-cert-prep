# Databricks notebook source
# MAGIC %md
# MAGIC # Extract Payments Data -   CSV via External Table 
# MAGIC
# MAGIC 1. Create a Volumne for external_data in gizmobox.landing
# MAGIC 2. List the files in the Payments folder.
# MAGIC 3. Create an External Table.
# MAGIC 4. Demo effects of Adding/Updating/Deleting Files.
# MAGIC 5. Demo effects of Dropping the Table.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Create a Volumne for external_data in gizmobox.landing

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC USE CATALOG gizmobox;
# MAGIC     
# MAGIC USE SCHEMA landing;
# MAGIC
# MAGIC CREATE VOLUME IF NOT EXISTS gizmobox.landing.external_data;
# MAGIC     -- EXTERNAL LOCATION 'url_str/landing/external_data/'    -- USE THIS IF USING AWS S3 / Azure ADLS

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. List the files in the Payments folder.

# COMMAND ----------

# MAGIC %fs ls '/Volumes/gizmobox/landing/external_data/payments/'

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC     *
# MAGIC FROM
# MAGIC     read_files('/Volumes/gizmobox/landing/external_data/payments/',
# MAGIC     format => 'csv',
# MAGIC     header => False,
# MAGIC     delimiter => ','
# MAGIC     )

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Create an External Table in gizmobox.bronze

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- CREATE TABLE IF NOT EXISTS gizmobox.bronze.payments
# MAGIC -- (
# MAGIC -- payment_id INTEGER,
# MAGIC -- order_id INTEGER,
# MAGIC -- payment_timestamp TIMESTAMP,
# MAGIC -- payment_status INTEGER,
# MAGIC -- payment_method STRING
# MAGIC -- );
# MAGIC
# MAGIC -- COPY INTO gizmobox.bronze.payments
# MAGIC -- FROM '/Volumes/gizmobox/landing/external_data/payments/'
# MAGIC -- FILEFORMAT = CSV
# MAGIC -- FORMAT_OPTIONS ('header' = 'true', 'delimiter' = ',')
# MAGIC -- COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

df = spark.read.csv(
    '/Volumes/gizmobox/landing/external_data/payments/',
    header=True,
    inferSchema=True
)

columns = ['payment_id', 'order_id', 'payment_timestamp', 'payment_status', 'payment_method']
df = df.toDF(*columns)

df.write.format('delta').mode('append').saveAsTable('gizmobox.bronze.payments')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gizmobox.bronze.payments

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE EXTENDED gizmobox.bronze.payments

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Demo effects of Adding/Updating/Deleting Files.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC NOTE: If we are creating an EXTERNAL TABLE, databricks creates a metadata of the files stored in the AWS S3 / Azure ADLS. 
# MAGIC
# MAGIC 1. Deleting a File - When a file is deleted from S3, the table needs to be refreshed again, or else it won't be able to read that EXTERNAL Table.
# MAGIC
# MAGIC 2. Adding a File - When a file is added in S3, the table needs to be refreshed again, or only the Previous Data will be shown.

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC REFRESH TABLE gizmobox.bronze.payments;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Demo effects of Dropping the Table.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC NOTE: IF the EXTERNAL TABLE IS DELETED/ DROP, only the Metadata of the table will be deleted, and the table will be availabe in the S3/ ADLS
# MAGIC
# MAGIC
# MAGIC %sql
# MAGIC DROP TABLE gizmobox.bronze.payments;