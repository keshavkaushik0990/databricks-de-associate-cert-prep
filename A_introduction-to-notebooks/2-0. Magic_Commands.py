# Databricks notebook source
# MAGIC %md
# MAGIC # Databricks Magic Commands

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC - %python
# MAGIC - %scala
# MAGIC - %r
# MAGIC - %sql
# MAGIC
# MAGIC ---- Will switch the language of the cell to the specified language
# MAGIC
# MAGIC - %md
# MAGIC
# MAGIC ---- Markdown

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC - %fs  : Run file system commands
# MAGIC - %sh  : Run Shell Commands (Driver Node Only)
# MAGIC - %pip : Install python libraries
# MAGIC - %run : Include / Import another notebook into the current notebook

# COMMAND ----------

# MAGIC %md
# MAGIC ## %fs : Run file systems

# COMMAND ----------

# MAGIC %fs

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

# MAGIC %fs ls dbfs:/databricks-datasets/

# COMMAND ----------

# MAGIC %md
# MAGIC ## %sh : Run Shell Commands (Driver Node Only)

# COMMAND ----------

# MAGIC %sh

# COMMAND ----------

# MAGIC %sh ps

# COMMAND ----------

# MAGIC %md
# MAGIC ## %pip : Install python libraries

# COMMAND ----------

# MAGIC %pip

# COMMAND ----------

# MAGIC %pip list

# COMMAND ----------

# MAGIC %pip install faker
# MAGIC
# MAGIC # faker Faker is an open-source Python package that generates realistic dummy data for testing, database bootstrapping, and privacy masking. It eliminates the need to manually write random text generation strings or maintain external static dictionaries of mock information.

# COMMAND ----------

# MAGIC %md
# MAGIC ## %run : Include / Import another notebook into the current notebook

# COMMAND ----------

# MAGIC %run "/Workspace/Users/keshavkaushik0990@gmail.com/learning_databricks/Databricks_Certified_Data_Engineer_Associate/A_introduction-to-notebooks/2.1 Enviornment_Variables_and_Functions"

# COMMAND ----------

print(env)

# COMMAND ----------

print_env_info()