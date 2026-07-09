-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Transform Memberships Data
-- MAGIC
-- MAGIC 1. Extract customer_id from the file path
-- MAGIC 2. Write transformed data to the Silver Schema

-- COMMAND ----------

SELECT
    path,
    modificationTime,
    length,
    content
FROM gizmobox.bronze.vw_memberships;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 1. Extract customer_id from the file path

-- COMMAND ----------

SELECT
    REPLACE(SPLIT(path, '/')[7], '.png', '') AS customer_id,
    path,
    modificationTime,
    length,
    content
FROM gizmobox.bronze.vw_memberships;

-- COMMAND ----------

SELECT
    regexp_extract(path , '.*/([0-9]+)\\.png$' , 1 ) AS customer_id,
    content AS membership_card
FROM gizmobox.bronze.vw_memberships;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 2. Write transformed data to the Silver Schema

-- COMMAND ----------

CREATE TABLE gizmobox.silver.memberships
AS (
SELECT
    regexp_extract(path , '.*/([0-9]+)\\.png$' , 1 ) AS customer_id,
    content AS membership_card
FROM gizmobox.bronze.vw_memberships
);

-- COMMAND ----------

SELECT * FROM gizmobox.silver.memberships;