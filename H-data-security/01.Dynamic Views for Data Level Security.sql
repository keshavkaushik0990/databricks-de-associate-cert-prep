-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Data-Level Security Using Dynamic Views
-- MAGIC
-- MAGIC This notebook demonstrates how data-level security can be implemented using dynamic views.
-- MAGIC
-- MAGIC The implementation covers two key capabilities:
-- MAGIC
-- MAGIC - Row-Level Security: Controls which rows are visible to a user  
-- MAGIC - Column-Level Masking: Controls how sensitive values are displayed  
-- MAGIC
-- MAGIC A simple sales dataset is used to illustrate how different users receive different results when querying the same view.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 1: Set up the schema for the table

-- COMMAND ----------

USE CATALOG demo;
CREATE SCHEMA IF NOT EXISTS data_security;

-- COMMAND ----------

USE SCHEMA data_security;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 2: Create the table
-- MAGIC A table is defined to represent sales data across multiple regions.

-- COMMAND ----------

CREATE OR REPLACE TABLE sales_dynamic (
  id INT,
  region STRING,
  email STRING,
  revenue INT
);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 3: Insert sample data
-- MAGIC The dataset includes records from both UK and US regions.
-- MAGIC
-- MAGIC This enables validation of row-level security by ensuring that different users see only relevant regional data.

-- COMMAND ----------

INSERT INTO sales_dynamic VALUES
  (1, 'UK', 'john.doe@email.com', 10000),
  (2, 'US', 'mike.smith@email.com', 20000),
  (3, 'UK', 'sara.jones@email.com', 15000),
  (4, 'US', 'david.brown@email.com', 25000),
  (5, 'UK', 'emma.wilson@email.com', 18000);

-- COMMAND ----------

SELECT * FROM sales_dynamic;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 4: Create the dynamic view
-- MAGIC The dynamic view implements both row-level security and column-level masking.
-- MAGIC
-- MAGIC ##### Row-Level Security
-- MAGIC
-- MAGIC - UK group → returns only rows where region = 'UK'  
-- MAGIC - US group → returns only rows where region = 'US'  
-- MAGIC - Admin group → returns all rows  
-- MAGIC
-- MAGIC ##### Column-Level Masking
-- MAGIC
-- MAGIC - Admin group → full email visible  
-- MAGIC - Other users → email is masked  
-- MAGIC
-- MAGIC ##### Key Function: is_account_group_member()
-- MAGIC
-- MAGIC This function evaluates whether the current user belongs to a specified group.
-- MAGIC
-- MAGIC Examples:
-- MAGIC
-- MAGIC - is_account_group_member('uk-sg') 
-- MAGIC - is_account_group_member('us-sg') 
-- MAGIC - is_account_group_member('admin-sg')  
-- MAGIC
-- MAGIC The function returns TRUE or FALSE and is used to drive conditional logic inside the view.

-- COMMAND ----------

SELECT is_account_group_member('admin-sg'), is_account_group_member('uk-sg')

-- COMMAND ----------

CREATE OR REPLACE VIEW vw_sales_dynamic AS
SELECT id,
       region,
       CASE 
         WHEN is_account_group_member('admin-sg') THEN email
         ELSE concat(substr(email, 1, 1), '***@', split(email, '@')[1])
       END AS email,  
       revenue
FROM sales_dynamic
WHERE is_account_group_member('admin-sg')
OR (is_account_group_member('uk-sg') AND region = 'UK')
OR (is_account_group_member('us-sg') AND region = 'US');

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Step 5: Query the dynamic view

-- COMMAND ----------

SELECT * FROM vw_sales_dynamic;

-- COMMAND ----------

SELECT * FROM vw_sales_dynamic;