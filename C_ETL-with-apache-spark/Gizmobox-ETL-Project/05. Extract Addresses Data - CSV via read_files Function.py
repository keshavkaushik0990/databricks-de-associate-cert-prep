# Databricks notebook source
# MAGIC %md
# MAGIC # Extract Data from Addresses Files
# MAGIC
# MAGIC 1. Limitations of CSV file format in SELECT Statement.
# MAGIC 2. Use read_files functions to overcome the limitations.
# MAGIC 3. Create Addresses View in Bronze Schema.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Limitations of CSV file format in SELECT Statement.

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM csv.`/Volumes/gizmobox/landing/operational_data/addresses/`

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Use read_files functions to overcome the limitations.

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC     *
# MAGIC FROM
# MAGIC     read_files('/Volumes/gizmobox/landing/operational_data/addresses/',
# MAGIC     format => 'csv',
# MAGIC     header => true,
# MAGIC     delimiter => '\t'
# MAGIC     )

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Create Addresses View in Bronze Schema.

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE VIEW gizmobox.bronze.vw_addresses AS 
# MAGIC (
# MAGIC SELECT
# MAGIC     *
# MAGIC FROM
# MAGIC     read_files('/Volumes/gizmobox/landing/operational_data/addresses/',
# MAGIC     format => 'csv',
# MAGIC     header => true,
# MAGIC     delimiter => '\t'
# MAGIC     )
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gizmobox.bronze.vw_addresses