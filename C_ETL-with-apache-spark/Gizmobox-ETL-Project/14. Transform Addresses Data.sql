-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Transform Addresses Data
-- MAGIC
-- MAGIC 1. Create One record for each customer with 2 sets of address column, 1 for Shipping and 1 for Billing Address
-- MAGIC 2. Write transformed data in Silver Schema

-- COMMAND ----------

SELECT
    customer_id,
    address_type,
    address_line_1,
    city,
    state,
    postcode,
    _rescued_data
FROM
    gizmobox.bronze.vw_addresses;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 1. Create One record for each customer with 2 sets of address column, 1 for Shipping and 1 for Billing Address

-- COMMAND ----------

SELECT *
FROM
    (
SELECT
    customer_id,
    address_type,
    address_line_1,
    city,
    state,
    postcode
FROM
    gizmobox.bronze.vw_addresses
    )
PIVOT
    (
    MAX(address_line_1) AS address_line_1,
    MAX(city) AS city,
    MAX(state) AS state,
    MAX(postcode) AS postcode
    FOR 
        address_type IN ('shipping', 'billing')
    )

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 2. Write transformed data in Silver Schema

-- COMMAND ----------

CREATE TABLE gizmobox.silver.addresses
AS
(
SELECT *
FROM
    (
SELECT
    customer_id,
    address_type,
    address_line_1,
    city,
    state,
    postcode
FROM
    gizmobox.bronze.vw_addresses
    )
PIVOT
    (
    MAX(address_line_1) AS address_line_1,
    MAX(city) AS city,
    MAX(state) AS state,
    MAX(postcode) AS postcode
    FOR 
        address_type IN ('shipping', 'billing')
    )
);

-- COMMAND ----------

SELECT * FROM gizmobox.silver.addresses;