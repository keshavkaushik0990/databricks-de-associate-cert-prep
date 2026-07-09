-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Transform Orders Data - Explode Arrayrs
-- MAGIC
-- MAGIC 1. Access Elements from the JSON object
-- MAGIC 2. Depuplicate Array Elements
-- MAGIC 3. Explode Arrays
-- MAGIC 4. Write the transformed Data to the Silver Schema

-- COMMAND ----------

SELECT
    json_value
FROM
    gizmobox.silver.orders_json;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 1. Access Elements from the JSON object

-- COMMAND ----------

SELECT
    json_value.order_id,
    json_value.order_date,
    json_value.order_status,
    json_value.payment_method,
    json_value.total_amount,
    json_value.transaction_timestamp,
    json_value.customer_id,
    json_value.items
FROM
    gizmobox.silver.orders_json;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 2. Depuplicate Array Elements

-- COMMAND ----------

SELECT
    json_value.order_id,
    json_value.order_date,
    json_value.order_status,
    json_value.payment_method,
    json_value.total_amount,
    json_value.transaction_timestamp,
    json_value.customer_id,
    array_distinct(json_value.items) AS items
FROM
    gizmobox.silver.orders_json;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 3. Explode Arrays

-- COMMAND ----------

CREATE VIEW IF NOT EXISTS vw_orders_exploded AS 
SELECT
    json_value.order_id,
    json_value.order_date,
    json_value.order_status,
    json_value.payment_method,
    json_value.total_amount,
    json_value.transaction_timestamp,
    json_value.customer_id,
    explode(array_distinct(json_value.items)) AS item
FROM
    gizmobox.silver.orders_json;

-- COMMAND ----------

SELECT
    * 
FROM 
    vw_orders_exploded;

-- COMMAND ----------

SELECT
    order_id,
    order_date,
    order_status,
    payment_method,
    total_amount,
    transaction_timestamp,
    customer_id,
    item.item_id,
    item.name,
    item.price,
    item.quantity,
    item.category,
    item.details.brand,
    item.details.color
FROM 
    vw_orders_exploded;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 4. Write the transformed Data to the Silver Schema

-- COMMAND ----------

CREATE OR REPLACE TABLE gizmobox.silver.orders 
AS
(
SELECT
    order_id,
    order_date,
    order_status,
    payment_method,
    total_amount,
    transaction_timestamp,
    customer_id,
    item.item_id,
    item.name,
    item.price,
    item.quantity,
    item.category,
    item.details.brand,
    item.details.color
FROM 
    vw_orders_exploded    
)
;

-- COMMAND ----------

SELECT * FROM gizmobox.silver.orders;