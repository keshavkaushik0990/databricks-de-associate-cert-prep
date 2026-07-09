# Databricks notebook source
# MAGIC %md
# MAGIC # Extract Payments Data - CSV via External Table
# MAGIC
# MAGIC 1. Create a refunds Table in gizmoboz.landing.refunds

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Create a refunds Table in gizmoboz.bronze

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS gizmobox.bronze.refunds (  
# MAGIC     refund_id INT PRIMARY KEY,  
# MAGIC     payment_id INT NOT NULL,  
# MAGIC     refund_timestamp TIMESTAMP NOT NULL,  
# MAGIC     refund_amount DECIMAL(10, 2) NOT NULL,  
# MAGIC     refund_reason VARCHAR(255) NOT NULL
# MAGIC );
# MAGIC
# MAGIC INSERT INTO gizmobox.bronze.refunds (refund_id, payment_id, refund_timestamp, refund_amount, refund_reason)  
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

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM gizmobox.bronze.refunds;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE EXTENDED gizmobox.bronze.refunds;

# COMMAND ----------

# MAGIC %md
# MAGIC # OLD METHOD - Hive Metastore
# MAGIC
# MAGIC 1. Create Bronze Schema in Hive Metastore
# MAGIC 2. Create External Table

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Create Bronze Schema in Hive Metastore

# COMMAND ----------

# MAGIC %sql
# MAGIC -- CREATE SCHEMA IF NOT EXISTS hive_metstore.bronze;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Create an External Table via JDBC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- CREATE TABLE IF NOT EXISTS hive_metstore.bronze.refunds;
# MAGIC -- USING JDBC
# MAGIC -- OPTIONS (
# MAGIC -- url 'jdbc......' ,
# MAGIC -- dbtable "refunds",
# MAGIC -- user 'username'
# MAGIC -- password 'password'
# MAGIC -- );