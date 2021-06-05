# Databricks notebook source
display(dbutils.fs.ls("/databricks-datasets"))

# COMMAND ----------

with open("/dbfs/databricks-datasets/README.md") as f:
    x = ''.join(f.readlines())

print(x)

# COMMAND ----------

# MAGIC %fs ls /databricks-datasets