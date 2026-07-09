# Databricks notebook source
# MAGIC %md
# MAGIC # Databricks Utilities
# MAGIC
# MAGIC - **File System utilities**
# MAGIC - **Secrets utilitie**s
# MAGIC - **Widget utilities**
# MAGIC - **Notebook Workflow utilities**

# COMMAND ----------

# MAGIC %md
# MAGIC ## File System utilities

# COMMAND ----------

# MAGIC %fs ls /

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

display(dbutils.fs.ls('/'))

# COMMAND ----------

# MAGIC %fs ls dbfs:/databricks-datasets/

# COMMAND ----------

item_lst =  dbutils.fs.ls("dbfs:/databricks-datasets/")

print(len(item_lst))

# COMMAND ----------

# Count folders and files using list comprehension
folders = len([item for item in item_lst if item.name.endswith('/')])
files = len([item for item in item_lst if not item.name.endswith('/')])

print(f"total folders: {folders}")
print(f"total files: {files}")

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.help('cp')