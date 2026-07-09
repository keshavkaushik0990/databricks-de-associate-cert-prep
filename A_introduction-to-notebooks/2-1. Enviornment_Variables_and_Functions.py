# Databricks notebook source
env = "test"

# COMMAND ----------

import os
import platform

def print_env_info():

    # Print Python version

    print(f"Python version: {platform.python_version()}")
    
    # Print Spark version

    print(f"Spark version: {spark.version}")
    
    # Print Databricks Runtime version

    runtime_version = os.environ.get("DATABRICKS_RUNTIME_VERSION")
    print(f"Databricks Runtime version: {runtime_version}")

# COMMAND ----------

# print_env_info()