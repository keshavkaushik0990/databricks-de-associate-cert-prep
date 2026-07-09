-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Transform Payments Data
-- MAGIC 1. Extract specific portion of the string from refund_reason using split function
-- MAGIC 2. Extract specific portion of the string from refund_reason using reg_exp_extract function
-- MAGIC 3. Extract Date and Time from refund_timestamp
-- MAGIC 4. Write transformed data to Silver Schema

-- COMMAND ----------


SELECT
    refund_id,
    payment_id,
    refund_timestamp,
    refund_amount,
    refund_reason
FROM
    gizmobox.bronze.refunds;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 1. Extract specific portion of the string from refund_reason using split function

-- COMMAND ----------


SELECT
    refund_id,
    payment_id,
    refund_timestamp,
    refund_amount,
    SPLIT(refund_reason, ':')[0] AS refund_reason,
    SPLIT(refund_reason, ':')[1] AS refund_source 
FROM
    gizmobox.bronze.refunds;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 2. Extract specific portion of the string from refund_reason using reg_exp_extract function

-- COMMAND ----------


SELECT
    refund_id,
    payment_id,
    refund_timestamp,
    refund_amount,
    regexp_extract(refund_reason, '^([^:]+):' , 1) AS refund_reason,
    regexp_extract(refund_reason, '^[^:]+:(.*)$' , 1) AS refund_source 
FROM
    gizmobox.bronze.refunds;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 3. Extract Date and Time from refund_timestamp

-- COMMAND ----------


SELECT
    refund_id,
    payment_id,
    CAST(DATE_FORMAT(refund_timestamp , 'yyyy-MM-dd') AS DATE ) AS refund_date,
    DATE_FORMAT(refund_timestamp , 'HH:mm:ss') AS refund_time,
    regexp_extract(refund_reason, '^([^:]+):' , 1) AS refund_reason,
    regexp_extract(refund_reason, '^[^:]+:(.*)$' , 1) AS refund_source 
FROM
    gizmobox.bronze.refunds;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 4. Write transformed data to Silver Schema

-- COMMAND ----------


CREATE TABLE gizmobox.silver.refunds
AS 
SELECT
    refund_id,
    payment_id,
    CAST(DATE_FORMAT(refund_timestamp , 'yyyy-MM-dd') AS DATE ) AS refund_date,
    DATE_FORMAT(refund_timestamp , 'HH:mm:ss') AS refund_time,
    regexp_extract(refund_reason, '^([^:]+):' , 1) AS refund_reason,
    regexp_extract(refund_reason, '^[^:]+:(.*)$' , 1) AS refund_source 
FROM
    gizmobox.bronze.refunds;

-- COMMAND ----------

SELECT * FROM gizmobox.silver.refunds;