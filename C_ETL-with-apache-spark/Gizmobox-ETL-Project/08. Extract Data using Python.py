# Databricks notebook source
# MAGIC %md
# MAGIC # Extract Data using Python
# MAGIC
# MAGIC 1. Run SQL commands using Python - spark.sql.functions
# MAGIC 2. Spark Dataframe Reader API
# MAGIC 3. Read Table using spark.table Function

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Run SQL commands using Python - spark.sql.functions

# COMMAND ----------

df = spark.sql("SELECT * FROM JSON.`/Volumes/gizmobox/landing/operational_data/customers/`")

display(df)

# COMMAND ----------

df = spark.sql('''CREATE OR REPLACE TEMPORARY VIEW vw_temp AS
               SELECT * FROM JSON.`/Volumes/gizmobox/landing/operational_data/customers/`''')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM vw_temp

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Spark Dataframe Reader API

# COMMAND ----------

df = spark.read.format("json").load("/Volumes/gizmobox/landing/operational_data/customers/")

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Read Table using spark.table Function

# COMMAND ----------

spark.table("gizmobox.bronze.vw_addresses").display()