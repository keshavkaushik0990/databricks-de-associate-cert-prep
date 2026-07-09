# Databricks notebook source
# MAGIC %md
# MAGIC # Check weather the Workspace is attached to a Unity Catalog Metastore

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT current_metastore()