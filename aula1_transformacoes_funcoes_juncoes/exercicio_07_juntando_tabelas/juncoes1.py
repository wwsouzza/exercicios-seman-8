import pandas as pd

import numpy as np

pedidos = pd.read_csv("pedidos.csv")
produtos = pd.read_csv("produtos.csv")
clientes = pd.read_csv("clientes.csv")

base = pedidos.merge(produtos, on= "id_produto", how="left", validate="m:1")
print(pedidos.shape, "->", base.shape)

cli_left = pedidos.merge(clientes, on= "id_cliente", how="left")
cli_inner = pedidos.merge(clientes, on= "id_cliente", how="inner")
print(len(pedidos), len(cli_left), len(cli_inner))
print(pedidos["id_cliente"].isna().sum(), "pedidos sem cliente" )

base["total"] = base["qtd"] * base["preco"]
base["lucro"] = base["qtd"] * (base["preco"] - base["custo"])
print(base[["produto", "qtd", "preco", "total", "lucro"]].head(3))
