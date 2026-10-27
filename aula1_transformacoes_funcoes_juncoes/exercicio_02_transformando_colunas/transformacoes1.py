import pandas as pd

import numpy as np

pedidos = pd.read_csv("pedidos.csv")

pedidos["data"] = pd.to_datetime(pedidos[ "data"])
pedidos["mes"] = pedidos["data"].dt.month
pedidos["dia_semana"] = pedidos["data"].dt.dayofweek
print(pedidos[["data", "mes", "dia_semana"]].head(3))
print(pedidos["data"].dtype)

pedidos["canal"] = pedidos["canal"].str.strip().str.title()
print(pedidos["canal"].value_counts())

dias = {0: "seg", 1: "ter", 2: "qua", 3: "qui", 4: "sex", 5: "sab", 6:
"dom"}
pedidos["dia"] = pedidos["dia_semana"].map(dias)
print(pedidos[["data", "dia_semana", "dia"]].head(3))