-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Data-Level Security Using Row Filters and Column Masks
-- MAGIC
-- MAGIC This notebook demonstrates how data-level security can be implemented directly on a table using row filters and column masks.
-- MAGIC
-- MAGIC Unlike dynamic views, where logic is defined within a view, this approach applies security rules directly to the table. These rules are enforced automatically whenever the table is queried.
-- MAGIC
-- MAGIC The implementation covers two key capabilities:
-- MAGIC
-- MAGIC - Row-Level Security: Controls which rows are visible to a user  
-- MAGIC - Column-Level Masking: Controls how sensitive values are displayed  
-- MAGIC
-- MAGIC A simple sales dataset is used to illustrate how different users receive different results when querying the same table
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

CREATE OR REPLACE TABLE sales_secured (
  id INT,
  region STRING,
  email STRING,
  revenue INT
);


-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 3: Insert Sample Data

-- COMMAND ----------

INSERT INTO sales_secured VALUES
  (1, 'UK', 'john.doe@email.com', 10000),
  (2, 'US', 'mike.smith@email.com', 20000),
  (3, 'UK', 'sara.jones@email.com', 15000),
  (4, 'US', 'david.brown@email.com', 25000),
  (5, 'UK', 'emma.wilson@email.com', 18000);

-- COMMAND ----------

SELECT * FROM sales_secured;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 4: Define Row Filter Function
-- MAGIC The function evaluates the user’s group membership and returns a condition that determines whether a row should be included in the result.
-- MAGIC
-- MAGIC For example:
-- MAGIC
-- MAGIC - Users in the UK group are allowed to view UK records
-- MAGIC - Users in the US group are allowed to view US records
-- MAGIC - Admin users are allowed to view all records

-- COMMAND ----------

CREATE OR REPLACE FUNCTION fn_filter_region (region STRING)
RETURN 
  is_account_group_member('admin-sg')
  OR (is_account_group_member('uk-sg') AND region = 'UK')
  OR (is_account_group_member('us-sg') AND region = 'US');

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 5: Apply Row Filter to Table
-- MAGIC The row filter function is attached to the table. Once applied, the function is evaluated automatically at query time, and only the rows that satisfy the condition are returned.

-- COMMAND ----------

ALTER TABLE sales_secured
SET ROW FILTER fn_filter_region ON (region);

-- COMMAND ----------

DESC EXTENDED sales_secured;

-- COMMAND ----------

SELECT * FROM sales_secured;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 6: Define Column Mask Function
-- MAGIC The function evaluates the user’s group membership and determines whether to return the original value or a masked version.
-- MAGIC
-- MAGIC For example:
-- MAGIC - Admin users can view the full email address
-- MAGIC - Other users see a masked version of the email

-- COMMAND ----------

CREATE OR REPLACE FUNCTION fn_mask_email (email STRING)
RETURN 
    CASE 
         WHEN is_account_group_member('admin-sg') THEN email
         ELSE concat(substr(email, 1, 1), '***@', split(email, '@')[1])
    END;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 7: Apply Column Mask
-- MAGIC The masking function is attached to the email column. Once applied, the function is executed automatically whenever the column is queried.

-- COMMAND ----------

ALTER TABLE sales_secured
ALTER COLUMN email SET MASK fn_mask_email;

-- COMMAND ----------

DESC EXTENDED sales_secured;

-- COMMAND ----------

SELECT * FROM sales_secured;