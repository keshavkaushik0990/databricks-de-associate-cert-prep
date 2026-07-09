# Databricks notebook source
# MAGIC %md
# MAGIC # Data Profilling in Databricks
# MAGIC
# MAGIC 1. Profile data using UI
# MAGIC 2. Profile data using dbutils Package (dbutils.data.summarize method)
# MAGIC 3. Profile data manually
# MAGIC
# MAGIC - COUNT
# MAGIC - COUNT_IF
# MAGIC - MIN
# MAGIC - MAX
# MAGIC - WHERE Clause

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Profile data using UI

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gizmobox.bronze.vw_customers;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Profile data using dbutils Package (dbutils.data.summarize method)

# COMMAND ----------

df = spark.table("gizmobox.bronze.vw_customers")

dbutils.data.summarize(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Profile data manually
# MAGIC
# MAGIC - COUNT
# MAGIC - COUNT_IF
# MAGIC - WHERE Clause
# MAGIC - DISTINCT Keyword

# COMMAND ----------

# MAGIC %md
# MAGIC ### COUNT()

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT COUNT(*) FROM gizmobox.bronze.vw_customers

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT COUNT(*), COUNT(customer_id), COUNT(email), COUNT(telephone) FROM gizmobox.bronze.vw_customers;

# COMMAND ----------

# MAGIC %md
# MAGIC ### COUNT_IF()

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT COUNT_IF(customer_id IS NULL), COUNT_IF(email IS NULL), COUNT_IF(telephone IS NULL) FROM gizmobox.bronze.vw_customers;

# COMMAND ----------

# MAGIC %md
# MAGIC ### WHERE Clause

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM gizmobox.bronze.vw_customers WHERE customer_id IS NULL;

# COMMAND ----------

# MAGIC %md
# MAGIC ### DISTINCT Keyword

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT COUNT(*) AS total_recored, COUNT(DISTINCT customer_id) AS unique_records FROM gizmobox.bronze.vw_customers WHERE customer_id IS NOT NULL;