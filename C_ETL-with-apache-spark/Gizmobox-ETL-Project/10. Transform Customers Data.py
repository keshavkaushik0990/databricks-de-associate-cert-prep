# Databricks notebook source
# MAGIC %md
# MAGIC # Transform Customer Data
# MAGIC
# MAGIC 1. Remove recordes with NULL customer_id
# MAGIC 2. Remove exact duplicate recordes
# MAGIC 3. Remove duplicate recordes based on created_timestamp
# MAGIC 4. CAST Columns to the correct Data Type
# MAGIC 5. Write transformed data to the Silver Schema

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Remove recordes with NULL customer_id

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gizmobox.bronze.vw_customers WHERE customer_id IS NOT NULL ORDER BY customer_id;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Remove exact duplicate recordes

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT DISTINCT * FROM gizmobox.bronze.vw_customers WHERE customer_id IS NOT NULL ORDER BY customer_id;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC      customer_id,
# MAGIC      MAX(created_timestamp),
# MAGIC      MAX(customer_name),
# MAGIC      MAX(date_of_birth),
# MAGIC      MAX(email),
# MAGIC      MAX(member_since),
# MAGIC      MAX(telephone)
# MAGIC FROM gizmobox.bronze.vw_customers 
# MAGIC WHERE 
# MAGIC     customer_id IS NOT NULL 
# MAGIC GROUP BY customer_id
# MAGIC ORDER BY customer_id;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMPORARY VIEW vw_customers_distinct
# MAGIC AS
# MAGIC SELECT DISTINCT * FROM gizmobox.bronze.vw_customers WHERE customer_id IS NOT NULL ORDER BY customer_id;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC     customer_id,
# MAGIC     MAX(created_timestamp) AS max_created_timestamp  
# MAGIC FROM
# MAGIC     vw_customers_distinct
# MAGIC GROUP BY customer_id

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Remove duplicate recordes based on created_timestamp

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC WITH cte_max AS (
# MAGIC SELECT
# MAGIC     customer_id,
# MAGIC     MAX(created_timestamp) AS max_created_timestamp  
# MAGIC FROM
# MAGIC     vw_customers_distinct
# MAGIC GROUP BY customer_id
# MAGIC )
# MAGIC SELECT
# MAGIC     A.*
# MAGIC FROM
# MAGIC     vw_customers_distinct A JOIN cte_max B ON A.customer_id = B.customer_id AND A.created_timestamp = B.max_created_timestamp

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. CAST Columns to the correct Data Type

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC WITH cte_max AS (
# MAGIC SELECT
# MAGIC     customer_id,
# MAGIC     MAX(created_timestamp) AS max_created_timestamp  
# MAGIC FROM
# MAGIC     vw_customers_distinct
# MAGIC GROUP BY customer_id
# MAGIC )
# MAGIC SELECT
# MAGIC     CAST(A.created_timestamp AS TIMESTAMP) AS created_timestamp,
# MAGIC     A.customer_id,
# MAGIC     A.customer_name,
# MAGIC     CAST(A.date_of_birth AS DATE) AS date_of_birth,
# MAGIC     A.email,
# MAGIC     CAST(A.member_since AS DATE) AS member_since,
# MAGIC     A.telephone
# MAGIC FROM
# MAGIC     vw_customers_distinct A 
# MAGIC JOIN
# MAGIC     cte_max B ON A.customer_id = B.customer_id AND A.created_timestamp = B.max_created_timestamp;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Write transformed data to the Silver Schema

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE gizmobox.silver.customers
# MAGIC AS
# MAGIC WITH cte_max AS (
# MAGIC SELECT
# MAGIC     customer_id,
# MAGIC     MAX(created_timestamp) AS max_created_timestamp  
# MAGIC FROM
# MAGIC     vw_customers_distinct
# MAGIC GROUP BY customer_id
# MAGIC )
# MAGIC SELECT
# MAGIC     CAST(A.created_timestamp AS TIMESTAMP) AS created_timestamp,
# MAGIC     A.customer_id,
# MAGIC     A.customer_name,
# MAGIC     CAST(A.date_of_birth AS DATE) AS date_of_birth,
# MAGIC     A.email,
# MAGIC     CAST(A.member_since AS DATE) AS member_since,
# MAGIC     A.telephone
# MAGIC FROM
# MAGIC     vw_customers_distinct A 
# MAGIC JOIN
# MAGIC     cte_max B ON A.customer_id = B.customer_id AND A.created_timestamp = B.max_created_timestamp;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gizmobox.silver.customers;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE EXTENDED gizmobox.silver.customers;