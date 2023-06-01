# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM silver.pizza_query.pedido

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM silver.pizza_query.item_pedido

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM silver.pizza_query.pedido
# MAGIC WHERE flKetchup = TRUE AND descUF = 'Rio de Janeiro'
