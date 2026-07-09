-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Query Orders Data as JSON Strings
-- MAGIC
-- MAGIC 1. Extract Top Level Column Values
-- MAGIC 2. Extract Array Elements
-- MAGIC 3. Extract Nested Column Values
-- MAGIC 4. CAST Column Values to a specific Data Type

-- COMMAND ----------

SELECT 
    value
FROM
    gizmobox.bronze.vw_orders;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 1. Extract Top Level Column Values

-- COMMAND ----------

SELECT 
    value:order_id AS order_id,
    value
FROM
    gizmobox.bronze.vw_orders;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 2. Extract Array Elements

-- COMMAND ----------

SELECT 
    value:items[0] AS item_1,
    value:items[1] AS item_2,
    value
FROM
    gizmobox.bronze.vw_orders;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 3. Extract Nested Column Values

-- COMMAND ----------

SELECT
    value:items[0] AS item_1,
    value:items[0].item_id AS item_1_item_id,
    value:items[1] AS item_2,
    value
FROM
    gizmobox.bronze.vw_orders;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 4. CAST Column Values to a specific Data Type

-- COMMAND ----------

SELECT
    value:items[0] AS item_1,
    value:items[0].item_id::INTEGER AS item_1_item_id,
    value:items[1] AS item_2,
    value
FROM
    gizmobox.bronze.vw_orders;