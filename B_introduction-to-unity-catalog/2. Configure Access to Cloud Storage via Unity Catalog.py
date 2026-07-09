# Databricks notebook source
# MAGIC %md
# MAGIC # Access Cloud Storage

# COMMAND ----------

url_str = "abfss://xyz@abcd.dfs.core.windows.net/"

# abfss://   - Protcol to access Azure Cloud 
# xyz        - Container Name in the Azure Data Lake Storage
# abcd       - ADLS Bucket Name in which the Container is created
# dfs.core.windows.net - ADLS Endpoint

# COMMAND ----------

# MAGIC %fs ls "url_str"

# COMMAND ----------

# MAGIC %md
# MAGIC # SQL Querry to create an External Locaiton

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE EXTERNAL LOCATION IF NOT EXISTS s3_bucket_name_to_create
# MAGIC     URL url_str
# MAGIC     WITH (STORAGE CREDENTIAL storage_credential_name)
# MAGIC     COMMENT "External Location for Demo"