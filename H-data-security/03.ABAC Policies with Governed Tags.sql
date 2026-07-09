-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Data-Level Security Using ABAC (Governed Tags)
-- MAGIC This notebook demonstrates how data-level security can be implemented using Attribute-Based Access Control (ABAC) in Unity Catalog.
-- MAGIC
-- MAGIC In previous examples, row filters and column masks were applied directly to individual tables. While effective, that approach requires policies to be defined and managed separately for each table.
-- MAGIC
-- MAGIC ABAC addresses this by introducing a centralized model where:
-- MAGIC
-- MAGIC - Data is tagged using governed attributes
-- MAGIC - Policies are defined once based on those attributes
-- MAGIC - Policies are applied automatically across multiple objects
-- MAGIC
-- MAGIC The objective is to:
-- MAGIC
-- MAGIC - Classify sensitive data using governed tags
-- MAGIC - Define reusable policies based on those tags
-- MAGIC
-- MAGIC > **Note:** Row filters and column masks are not supported on Dedicated (Single User) clusters as of now.
-- MAGIC > Use a Shared cluster or a Serverless cluster to run this demo.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 1: Set up the schema for the table

-- COMMAND ----------

USE CATALOG demo;
USE SCHEMA data_security;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 2: Create the table
-- MAGIC A table is defined to represent sales data across multiple regions.

-- COMMAND ----------

CREATE OR REPLACE TABLE sales_abac (
  id INT,
  region STRING,
  email STRING,
  revenue INT
);


-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 3: Insert Sample Data

-- COMMAND ----------

INSERT INTO sales_abac VALUES
  (1, 'UK', 'john.doe@email.com', 10000),
  (2, 'US', 'mike.smith@email.com', 20000),
  (3, 'UK', 'sara.jones@email.com', 15000),
  (4, 'US', 'david.brown@email.com', 25000),
  (5, 'UK', 'emma.wilson@email.com', 18000);

-- COMMAND ----------

SELECT * FROM sales_abac;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 4: Create UDFs for row filter and column mask  
-- MAGIC (We have already created them as part of previous lecture)
-- MAGIC 1. `fn_filter_region` (This function evaluates the user’s group membership and determines whether to include a specifc record in the output based on the region)
-- MAGIC 1. `fn_mask_email` (This function evaluates the user’s group membership and determines whether to return the original value or a masked version of the value)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 5: Create Governed Tags
-- MAGIC 1. `pii = email` (Indicates that the data contains personally identifiable information (PII))
-- MAGIC 1. `access_type = region` (Defines the type of access control to be applied to the data, such as region-based or department-based filtering)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 6: Create Policy 
-- MAGIC (Could be at catalog/ schema/ table level)
-- MAGIC 1. policy_filter_region
-- MAGIC 1. policy_mask_email

-- COMMAND ----------

CREATE OR REPLACE POLICY `policy_filter_region`
ON SCHEMA demo.data_security
ROW FILTER demo.data_security.fn_filter_region
TO `uk-sg`
FOR TABLES
MATCH COLUMNS has_tag_value('access_type','region') AS u1
USING COLUMNS (u1)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 7: Attach tags to the table
-- MAGIC 1. sales_abac.region
-- MAGIC 1. sales_abac.email

-- COMMAND ----------

SELECT * FROM sales_abac;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 8: Create another table to demonstrate scalability of the ABAC implementation

-- COMMAND ----------

CREATE OR REPLACE TABLE customers_abac (
  customer_id INT,
  customer_name STRING,
  email STRING,
  region STRING
);

-- COMMAND ----------

ALTER TABLE customers_abac
ALTER COLUMN email
SET TAGS ('pii' = 'email');

-- COMMAND ----------

ALTER TABLE customers_abac
ALTER COLUMN region
SET TAGS ('access_type' = 'region');

-- COMMAND ----------

INSERT INTO customers_abac VALUES
  (1, 'John Smith', 'john.smith@email.com', 'UK'),
  (2, 'Mike Johnson', 'mike.johnson@email.com', 'US'),
  (3, 'Sara Jones', 'sara.jones@email.com', 'UK'),
  (4, 'David Brown', 'david.brown@email.com', 'US');

-- COMMAND ----------

SELECT * FROM customers_abac;