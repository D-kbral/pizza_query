# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC SELECT 
# MAGIC COUNT(*),       -- linhjas não nulas
# MAGIC COUNT(1),       -- linhas não nulas
# MAGIC COUNT(idPedido) -- linhas não nulas da coluna pedido 
# MAGIC FROM silver.pizza_query.pedido

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT count(*)
# MAGIC FROM silver.pizza_query.pedido
# MAGIC WHERE flKetchup IS NOT null

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT count(*)
# MAGIC FROM silver.pizza_query.pedido
# MAGIC WHERE descUF = 'Roraima'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC descUF,
# MAGIC count(*) as qtdePedidos
# MAGIC FROM silver.pizza_query.pedido
# MAGIC GROUP BY descUF
# MAGIC ORDER BY qtdePedidos DESC
# MAGIC LIMIT 6

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM silver.pizza_query.produto
# MAGIC WHERE descItem LIKE 'suco%'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC descUF,
# MAGIC count(*) AS qtdePedidos
# MAGIC FROM silver.pizza_query.pedido
# MAGIC WHERE descUF != 'São Paulo'
# MAGIC GROUP BY descUF
# MAGIC HAVING qtdePedidos >= 75
# MAGIC ORDER BY qtdePedidos DESC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC descUF,
# MAGIC flKetchup,
# MAGIC count(*)
# MAGIC FROM silver.pizza_query.pedido
# MAGIC GROUP BY descUF, flKetchup
# MAGIC ORDER BY descUF, flKetchup
