-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Transform Payments Data
-- MAGIC
-- MAGIC 1. Extract Date and Time from payment_timestamp and create new columns payment_date and payment _time
-- MAGIC 2. Map payment_status to contain descriptive values
-- MAGIC (1-Success, 2-Pending, 3-Cancelled, 4-Failed)
-- MAGIC 3. Write transformed data to Silver Schema

-- COMMAND ----------

SELECT
    payment_id,
    order_id,
    payment_timestamp,
    payment_status,
    payment_method
FROM
    gizmobox.bronze.payments;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 1. Extract Date and Time from payment_timestamp

-- COMMAND ----------

SELECT
    payment_id,
    order_id,
    payment_timestamp,
    CAST(DATE_FORMAT(payment_timestamp, 'yyyy-MM-dd') AS DATE ) AS payment_date,
    DATE_FORMAT(payment_timestamp, 'HH:mm:ss') AS payment_time,
    payment_status,
    payment_method
FROM
    gizmobox.bronze.payments;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 2. Map payment_status to contain descriptive values
-- MAGIC (1-Success, 2-Pending, 3-Cancelled, 4-Failed)

-- COMMAND ----------

SELECT
    payment_id,
    order_id,
    payment_timestamp,
    CAST(DATE_FORMAT(payment_timestamp, 'yyyy-MM-dd') AS DATE ) AS payment_date,
    DATE_FORMAT(payment_timestamp, 'HH:mm:ss') AS payment_time,
    CASE payment_status
        WHEN 1 THEN 'Success'
        WHEN 2 THEN 'Pending'
        WHEN 3 THEN 'Cancelled'
        WHEN 4 THEN 'Failed'
    END AS payment_status,
    payment_method
FROM
    gizmobox.bronze.payments;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 3. Write transformed data to Silver Schema 

-- COMMAND ----------

CREATE TABLE gizmobox.silver.payments
AS
SELECT
    payment_id,
    order_id,
    payment_timestamp,
    CAST(DATE_FORMAT(payment_timestamp, 'yyyy-MM-dd') AS DATE ) AS payment_date,
    DATE_FORMAT(payment_timestamp, 'HH:mm:ss') AS payment_time,
    CASE payment_status
        WHEN 1 THEN 'Success'
        WHEN 2 THEN 'Pending'
        WHEN 3 THEN 'Cancelled'
        WHEN 4 THEN 'Failed'
    END AS payment_status,
    payment_method
FROM
    gizmobox.bronze.payments;

-- COMMAND ----------

SELECT * FROM gizmobox.silver.payments;