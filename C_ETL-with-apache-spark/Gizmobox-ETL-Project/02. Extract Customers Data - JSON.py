# Databricks notebook source
# MAGIC %md
# MAGIC # Extract Data from Customers JSON File
# MAGIC
# MAGIC 1. Query Single File
# MAGIC 2. Query List of Files using Wild Card Characters
# MAGIC 3. Query all the files in a Folder

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Query Single File

# COMMAND ----------

# MAGIC %fs ls '/Volumes/gizmobox/landing/operational_data/customers/'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM JSON.`dbfs:/Volumes/gizmobox/landing/operational_data/customers/customers_2024_10.json` 

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Query Single File

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM JSON.`dbfs:/Volumes/gizmobox/landing/operational_data/customers/customers_2024*json` 

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Query all the files in a Folder

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM JSON.`dbfs:/Volumes/gizmobox/landing/operational_data/customers/*`

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. SELECT File Metadata

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC     -- input_file_name(),    -- This is the method is deprecated from Databricks Runtime 13.3 LTS onwards
# MAGIC     _metadata.file_path,
# MAGIC     _metadata AS meta_data,
# MAGIC     _metadata.file_path AS file_path,
# MAGIC     * 
# MAGIC FROM 
# MAGIC     JSON.`dbfs:/Volumes/gizmobox/landing/operational_data/customers/*`

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Register Files in the Unity Catalog using Views

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE VIEW gizmobox.bronze.vw_customers AS  (
# MAGIC SELECT
# MAGIC     *,
# MAGIC     _metadata.file_path AS file_path 
# MAGIC FROM 
# MAGIC     JSON.`dbfs:/Volumes/gizmobox/landing/operational_data/customers/*`
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gizmobox.bronze.vw_customers

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Create TEMPORARY View

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMPORARY VIEW vw_customers_TEMP AS  (
# MAGIC SELECT
# MAGIC     *,
# MAGIC     _metadata.file_path AS file_path 
# MAGIC FROM 
# MAGIC     JSON.`dbfs:/Volumes/gizmobox/landing/operational_data/customers/*`
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM vw_customers_TEMP

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Create GLOBAL TEMPORARY View

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- GLOBAL TEMPORARY VIEW is not supported on serverless compute.
# MAGIC
# MAGIC CREATE OR REPLACE GLOBAL TEMPORARY VIEW vw_customers_GLOBAL_TEMP AS  (
# MAGIC SELECT
# MAGIC     *,
# MAGIC     _metadata.file_path AS file_path 
# MAGIC FROM 
# MAGIC     JSON.`dbfs:/Volumes/gizmobox/landing/operational_data/customers/*`
# MAGIC )

# COMMAND ----------

# MAGIC %md
# MAGIC NOTE : All the GLOBAL TEMPORARY VIEW are stored in global_temp schema by default

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM global_temp.vw_customers_GLOBAL_TEMP