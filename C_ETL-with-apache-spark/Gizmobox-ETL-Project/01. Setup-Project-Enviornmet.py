# Databricks notebook source
# MAGIC %md
# MAGIC # Gizmobox ETL Project

# COMMAND ----------

# MAGIC %md
# MAGIC ## Setting up Project Enviornment

# COMMAND ----------

# MAGIC %md
# MAGIC ---------------------------------------    FOR AWS S3/ Azure ADLS    ---------------------------------------
# MAGIC
# MAGIC Skip 1 & 2 if you are using Databricks Free Edition

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Access the container gizmobox

# COMMAND ----------

# MAGIC %fs ls "abfss://xyz@abcd.dfs.core.windows.net/"

# COMMAND ----------

url_str = "abfss://xyz@abcd.dfs.core.windows.net/"

# abfss://   - Protcol to access Azure Cloud 
# xyz        - Container Name in the Azure Data Lake Storage
# abcd       - ADLS Bucket Name in which the Container is created
# dfs.core.windows.net - ADLS Endpoint

# COMMAND ----------

# %fs ls "url_str"

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Create External Location

# COMMAND ----------

# %sql

# CREATE EXTERNAL LOCATION IF NOT EXISTS s3_bucket_name_to_create
#     URL url_str
#     WITH (STORAGE CREDENTIAL storage_credential_name)
#     COMMENT "External Location for Demo"

# COMMAND ----------

# MAGIC %md
# MAGIC ---------------------------------------    FOR AWS S3/ Azure ADLS    ---------------------------------------

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Create a new Catalog - gizmobox

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW CATALOGS;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS gizmobox
# MAGIC     -- MANAGED LOCATION 'external_location_path'    -- if this is not added then the catalog will be in the root storage of the unity catalog
# MAGIC     COMMENT 'Catalog for GizmoBox'

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW CATALOGS;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Create Schemas under the Catalog 
# MAGIC
# MAGIC 1. Landing / RAW
# MAGIC 2. Bronze
# MAGIC 3. Silver
# MAGIC 4. Gold

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT current_catalog();

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG gizmobox;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT current_catalog();

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS gizmobox.landing
# MAGIC     -- MANAGED LOCATION 'external_location_path'    -- if this is not added then the catalog will be in the root storage of the unity catalog
# MAGIC     -- MANAGED LOCATION 'external_location_path'    -- THIS IS IF WE NOT NOT USING UNITY CATALOG
# MAGIC     COMMENT 'This is considered as the RAW data from the Data Warehouse of the company Gizmobox'

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE SCHEMA EXTENDED landing; 

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS gizmobox.bronze;
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS gizmobox.silver;
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS gizmobox.gold;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW SCHEMAS;

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Create Volume

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG gizmobox;
# MAGIC     
# MAGIC USE SCHEMA landing;
# MAGIC
# MAGIC CREATE VOLUME IF NOT EXISTS gizmobox.landing.operational_data;
# MAGIC     -- EXTERNAL LOCATION 'url_str/landing/operational_data/'    -- USE THIS IF USING AWS S3 / Azure ADLS            

# COMMAND ----------

# MAGIC %fs ls '/Volumes/gizmobox/landing/operational_data/'