import pandas as pd
import numpy as np

pedidos = pd.read_csv("pedidos.csv")

print(pedidos.shape)
print(pedidos[["id_pedido", "data", "qtd", "canal"]].head(3))

# Converter a coluna "data" para o tipo datetime
pedidos["data"] = pd.to_datetime(pedidos["data"])
print(pedidos[["data"]].head(3))
pedidos["mes"] = pedidos["data"].dt.month
pedidos["dia_semana"] = pedidos["data"].dt.dayofweek
print(pedidos.head(3))

#Padronização
pedidos["canal"] = pedidos["canal"].str.strip().str.title()
print(pedidos["canal"].value_counts())


