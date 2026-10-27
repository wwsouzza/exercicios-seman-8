import pandas as pd

import numpy as np

pedidos = pd.read_csv("pedidos.csv")

pedidos["pedido_grande" ] = np.where(pedidos[ "qtd"] >= 3, "sim", "não")
print(pedidos["pedido_grande" ].value_counts())

faixas = pd.cut(
 pedidos["tempo_entrega_min"],
 bins=[0, 20, 30, 45, np.inf],
 labels=["até 20", "21-30", "31-45", "mais de 45"],
)
print(faixas.value_counts().sort_index())
