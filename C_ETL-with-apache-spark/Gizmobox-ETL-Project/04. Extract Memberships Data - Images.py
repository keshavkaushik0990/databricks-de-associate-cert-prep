# Databricks notebook source
# MAGIC %md
# MAGIC # Extract Data from Orders JSON File
# MAGIC
# MAGIC 1. Query Memberships File using binaryFile Format
# MAGIC 2. Create Memberships View in Bronze Schema

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Query Memberships File using binaryFile Format

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM binaryFile.`/Volumes/gizmobox/landing/operational_data/memberships/*/*.png`

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Create Memberships View in Bronze Schema

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE VIEW gizmobox.bronze.vw_memberships AS 
# MAGIC (
# MAGIC SELECT * FROM binaryFile.`/Volumes/gizmobox/landing/operational_data/memberships/*/*.png`  
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gizmobox.bronze.vw_memberships