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

# COMMAND ----------

Dtt = spark.sql("""
select date_sub(current_timestamp(), 30)                
""").collect()[0][0]
print(f"{Dtt}")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC idPedido,
# MAGIC trim(cast(dtPedido AS DATE)) as data_pedido,
# MAGIC descUF
# MAGIC FROM silver.pizza_query.pedido
# MAGIC WHERE descUF = 'São Paulo' AND data_pedido = '{Dtt}'
