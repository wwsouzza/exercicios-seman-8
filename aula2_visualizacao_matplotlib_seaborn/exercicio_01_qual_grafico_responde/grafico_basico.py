

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()

plt.rcParams["figure.figsize"] = (6, 4)

# Carrega o CSV usando o caminho da pasta onde o script está salvo
base = pd.read_csv(BASE / "pedidos_prontos.csv", parse_dates=["data"])

# 1. Agrupamento: contagem de pedidos por mês
mensal = base.groupby("mes").size()

# 2. Plotagem do gráfico de linha
plt.plot(mensal.index, mensal.values, marker="o")
plt.show()


# 1. Agrupamento: soma do faturamento (total) por canal de venda
por_cat = base.groupby( "categoria")["total"].sum()
por_cat = por_cat.sort_values()
print(por_cat.round(0))
# 2. Plotagem do gráfico de barras
plt.barh(por_cat.index, por_cat.values)
plt.show()

entrega = base.dropna(subset=["tempo_entrega_min", "avaliacao"])
print(len(entrega), "entregas com nota")
print(entrega[["tempo_entrega_min", "avaliacao"]].describe().round(1))

plt.scatter(
 entrega["tempo_entrega_min"],
 entrega["avaliacao"],
 alpha=0.5,
)
plt.show()




