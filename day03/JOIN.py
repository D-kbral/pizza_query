# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM silver.pizza_query.item_pedido
# MAGIC ORDER BY RAND() 
# MAGIC limit 100

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC t1.idPedido, 
# MAGIC SUM(t2.vlPreco) AS vlPedido
# MAGIC
# MAGIC FROM silver.pizza_query.item_pedido AS t1
# MAGIC
# MAGIC LEFT JOIN silver.pizza_query.produto AS t2
# MAGIC ON t1.descItem = t2.descItem
# MAGIC
# MAGIC WHERE t1.descTipoItem <> 'bebida'
# MAGIC
# MAGIC GROUP BY t1.idPedido
