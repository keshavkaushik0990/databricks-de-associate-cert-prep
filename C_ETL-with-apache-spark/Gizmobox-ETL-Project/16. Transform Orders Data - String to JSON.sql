-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Transform Orders Data - String to JSON
-- MAGIC
-- MAGIC 1. Pre-process the JSON String to fix the Data Quality Issue
-- MAGIC 2. Tranform JSON String to JSON Object
-- MAGIC 3. Write transformed data to the silver schema

-- COMMAND ----------

SELECT
    value
FROM
    gizmobox.bronze.vw_orders;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 1. Pre-process the JSON String to fix the Data Quality Issue

-- COMMAND ----------

SELECT
    regexp_replace(value, '"order_date": (\\d{4}-\\d{2}-\\d{2})' , '"order_date":"\$1"') AS fixed_value,
    value
FROM
    gizmobox.bronze.vw_orders;

-- COMMAND ----------

CREATE OR REPLACE TEMP VIEW t_vw_orders_fixed
AS
(
SELECT
    regexp_replace(value, '"order_date": (\\d{4}-\\d{2}-\\d{2})' , '"order_date":"\$1"') AS fixed_value,
    value
FROM
    gizmobox.bronze.vw_orders
)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 2. Tranform JSON String to JSON Object

-- COMMAND ----------

SELECT
    schema_of_json(fixed_value) AS schema,
    fixed_value
FROM
    t_vw_orders_fixed

-- COMMAND ----------

-- STRUCT<customer_id: BIGINT, items: ARRAY<STRUCT<category: STRING, details: STRUCT<brand: STRING, color: STRING>, item_id: BIGINT, name: STRING, price: BIGINT, quantity: BIGINT>>, order_date: STRING, order_id: BIGINT, order_status: STRING, payment_method: STRING, total_amount: BIGINT, transaction_timestamp: STRING>


SELECT
    from_json(fixed_value , 'STRUCT<customer_id: BIGINT, items: ARRAY<STRUCT<category: STRING, details: STRUCT<brand: STRING, color: STRING>, item_id: BIGINT, name: STRING, price: BIGINT, quantity: BIGINT>>, order_date: STRING, order_id: BIGINT, order_status: STRING, payment_method: STRING, total_amount: BIGINT, transaction_timestamp: STRING>') AS json_value,
    fixed_value
FROM
    t_vw_orders_fixed

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 3. Write transformed data to the silver schema

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS gizmobox.silver.orders_json
AS
(
SELECT
    from_json(fixed_value , 'STRUCT<customer_id: BIGINT, items: ARRAY<STRUCT<category: STRING, details: STRUCT<brand: STRING, color: STRING>, item_id: BIGINT, name: STRING, price: BIGINT, quantity: BIGINT>>, order_date: STRING, order_id: BIGINT, order_status: STRING, payment_method: STRING, total_amount: BIGINT, transaction_timestamp: STRING>') AS json_value
FROM
    t_vw_orders_fixed
)

-- COMMAND ----------

SELECT * FROM gizmobox.silver.orders_json;