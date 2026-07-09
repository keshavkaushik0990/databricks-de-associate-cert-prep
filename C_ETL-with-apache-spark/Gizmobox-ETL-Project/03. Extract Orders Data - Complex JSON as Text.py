# Databricks notebook source
# MAGIC %md
# MAGIC # Extract Data from Orders JSON File
# MAGIC
# MAGIC 1. Query Orders File using JSON Format
# MAGIC 2. Query Orders File using TEXT Format
# MAGIC 3. Create Orders View in Bronze Schema

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Query Orders File using JSON Format

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM JSON.`dbfs:/Volumes/gizmobox/landing/operational_data/orders/*` 

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Query Orders File using TEXT Format

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM TEXT.`dbfs:/Volumes/gizmobox/landing/operational_data/orders/*`

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Create Orders View in Bronze Schema

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE VIEW gizmobox.bronze.vw_orders AS 
# MAGIC (
# MAGIC SELECT * FROM TEXT.`dbfs:/Volumes/gizmobox/landing/operational_data/orders/*`    
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gizmobox.bronze.vw_orders