# Databricks notebook source
# MAGIC %md
# MAGIC # Debugging Databricks Notebooks

# COMMAND ----------

# MAGIC %md
# MAGIC Enable Debugger: Settings -> Developer -> Enable Python Notebook interactive debugger
# MAGIC
# MAGIC Note :- 
# MAGIC
# MAGIC Supported Runtime - 13.3 LTS or Higher
# MAGIC
# MAGIC Supported Languages - Python only at the moment

# COMMAND ----------

# MAGIC %md
# MAGIC ## Demo 1

# COMMAND ----------

# MAGIC %md
# MAGIC 1. Breakpoints
# MAGIC 2. Step through code line by line
# MAGIC 3. Variable Explorer
# MAGIC 4. Debug Console

# COMMAND ----------

# Calculate the final price of an item and print the final total

item_price = 120.00
tax_rate   = 20          # given as %age
discount   = 10.00

# 1. Calculate the tax to be applied 
tax = item_price * (tax_rate / 100)

# 2. Applt tax to item price
item_price_w_tax = item_price - tax

# 3. Calculate the final price after discount
final_price = item_price_w_tax - discount

# 4. Print the final price
print("Final price:- " ,final_price)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Demo 2

# COMMAND ----------

# MAGIC %md
# MAGIC 5. Step In
# MAGIC 6. Step Out

# COMMAND ----------

def find_final_price(item_price, tax_rate, discount):
    # 1. Calculate the tax to be applied 
    tax = item_price * (tax_rate / 100)

    # 2. Applt tax to item price
    item_price_w_tax = item_price - tax

    # 3. Calculate the final price after discount
    final_price = item_price_w_tax - discount

    return final_price

# COMMAND ----------

item_price = 120.00
tax_rate   = 20          # given as %age
discount   = 10.00

final_price = find_final_price(item_price, tax_rate, discount)

print("Final price:- " ,final_price)