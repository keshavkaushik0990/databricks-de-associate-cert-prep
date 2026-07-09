# Databricks notebook source
# MAGIC %md
# MAGIC ## Extract Data From the Returns SQL Table
# MAGIC 1. Read Returns Data via JDBC
# MAGIC 2. Create Returns Table in Bronze Schema

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Read Returns Data via JDBC

# COMMAND ----------

# df = (
#   spark.read.format('jdbc')
#        .option('url', 'jdbc:sqlserver://gizmobox-srv.database.windows.net:1433;database=gizmobox-db')
#        .option('dbtable', 'refunds')
#        .option('user', 'gizmoboxadm')
#        .option('password', 'Gizmobox@Adm')
#        .load()
# )
# display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### via SQL

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS gizmobox.bronze.py_refunds (  
# MAGIC     refund_id INT PRIMARY KEY,  
# MAGIC     payment_id INT NOT NULL,  
# MAGIC     refund_timestamp TIMESTAMP NOT NULL,  
# MAGIC     refund_amount DECIMAL(10, 2) NOT NULL,  
# MAGIC     refund_reason VARCHAR(255) NOT NULL
# MAGIC );
# MAGIC
# MAGIC INSERT INTO gizmobox.bronze.py_refunds (refund_id, payment_id, refund_timestamp, refund_amount, refund_reason)  
# MAGIC VALUES  
# MAGIC (1, 66, '2025-01-10 11:30:00', 85.75, 'Payment Error:Retailer'),  
# MAGIC (2, 69, '2025-01-03 12:40:15', 120.50, 'Order Cancelled:Customer'),  
# MAGIC (3, 72, '2025-01-06 14:45:30', 65.00, 'Product Returned:Customer'),  
# MAGIC (4, 73, '2025-01-07 16:10:45', 210.99, 'Order Cancelled:Customer'),  
# MAGIC (5, 75, '2025-01-09 18:25:00', 45.20, 'Payment Error:Retailer'),  
# MAGIC (6, 80, '2025-01-10 09:35:20', 130.15, 'Order Cancelled:Customer'),  
# MAGIC (7, 83, '2025-01-12 11:20:40', 150.00, 'Product Returned:Customer'),  
# MAGIC (8, 85, '2025-01-14 13:15:30', 89.99, 'Order Cancelled:Customer'),  
# MAGIC (9, 89, '2025-01-15 15:00:00', 78.50, 'Payment Error:Retailer'),  
# MAGIC (10, 91, '2025-01-17 16:45:15', 250.75, 'Product Returned:Customer');

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Write the refunds data to the bronze schema

# COMMAND ----------

# df.writeTo('gizmobox.bronze.py_refunds').createOrReplace()

# COMMAND ----------

# MAGIC %sql
# MAGIC -- SELECT * FROM hive_metastore.bronze.py_refunds;
# MAGIC
# MAGIC SELECT * FROM gizmobox.bronze.py_refunds;