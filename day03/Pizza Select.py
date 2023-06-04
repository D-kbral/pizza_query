# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC descItem,
# MAGIC count(*) AS qtdePedido
# MAGIC FROM silver.pizza_query.item_pedido
# MAGIC WHERE descTipoItem = 'borda'
# MAGIC GROUP BY descItem
# MAGIC ORDER BY qtdePedido DESC
# MAGIC limit 1

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC descItem,
# MAGIC count(*) AS qtdePedido
# MAGIC FROM silver.pizza_query.item_pedido
# MAGIC WHERE descTipoItem = 'massa'
# MAGIC GROUP BY descItem
# MAGIC ORDER BY qtdePedido DESC
# MAGIC limit 1

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC descItem,
# MAGIC count(*) AS qtdePedido
# MAGIC FROM silver.pizza_query.item_pedido
# MAGIC WHERE descTipoItem LIKE '%queijo%'
# MAGIC GROUP BY descItem
# MAGIC ORDER BY qtdePedido DESC
# MAGIC limit 1

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC descItem,
# MAGIC count(*) AS qtdePedido
# MAGIC FROM silver.pizza_query.item_pedido
# MAGIC WHERE descTipoItem LIKE '%ingrediente%'
# MAGIC GROUP BY descItem
# MAGIC ORDER BY qtdePedido DESC
# MAGIC limit 5

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC descItem,
# MAGIC count(*) AS qtdePedido
# MAGIC FROM silver.pizza_query.item_pedido
# MAGIC WHERE descTipoItem LIKE '%bebida%'
# MAGIC GROUP BY descItem
# MAGIC ORDER BY qtdePedido DESC
# MAGIC limit 1

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC --sum(vlPreco)
# MAGIC FROM(
# MAGIC
# MAGIC (SELECT
# MAGIC descItem,
# MAGIC count(*) AS qtdePedido
# MAGIC FROM silver.pizza_query.item_pedido
# MAGIC WHERE descTipoItem = 'borda'
# MAGIC GROUP BY descItem
# MAGIC ORDER BY qtdePedido DESC
# MAGIC limit 1)
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC (SELECT 
# MAGIC descItem,
# MAGIC count(*) AS qtdePedido
# MAGIC FROM silver.pizza_query.item_pedido
# MAGIC WHERE descTipoItem = 'massa'
# MAGIC GROUP BY descItem
# MAGIC ORDER BY qtdePedido DESC
# MAGIC limit 1)
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC (SELECT 
# MAGIC descItem,
# MAGIC count(*) AS qtdePedido
# MAGIC FROM silver.pizza_query.item_pedido
# MAGIC WHERE descTipoItem LIKE '%queijo%'
# MAGIC GROUP BY descItem
# MAGIC ORDER BY qtdePedido DESC
# MAGIC limit 1)
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC (SELECT 
# MAGIC descItem,
# MAGIC count(*) AS qtdePedido
# MAGIC FROM silver.pizza_query.item_pedido
# MAGIC WHERE descTipoItem LIKE '%ingrediente%'
# MAGIC GROUP BY descItem
# MAGIC ORDER BY qtdePedido DESC
# MAGIC limit 5)
# MAGIC
# MAGIC UNION ALL
# MAGIC
# MAGIC (SELECT 
# MAGIC descItem,
# MAGIC count(*) AS qtdePedido
# MAGIC FROM silver.pizza_query.item_pedido
# MAGIC WHERE descTipoItem LIKE '%bebida%'
# MAGIC GROUP BY descItem
# MAGIC ORDER BY qtdePedido DESC
# MAGIC limit 1)
# MAGIC ) AS t1
# MAGIC
# MAGIC LEFT JOIN silver.pizza_query.produto AS t2
# MAGIC ON t1.descItem = t2.descItem
