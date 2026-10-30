from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

base = pd.read_csv(BASE / "pedidos_prontos.csv", parse_dates=["data"])

# Criando uma matriz 2x2 de eixos (axes)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 7), layout="constrained")

sns.lineplot(
    data=base,
    x="mes",
    y="total",
    estimator="sum",
    errorbar=None,
    marker="o",
    color="#2b5c8f",
    ax=axes[0, 0]
)
axes[0, 0].set_title("1. Faturamento por Mês")
axes[0, 0].set_xlabel("Mês")
axes[0, 0].set_ylabel("Faturamento Total (R$)")

sns.barplot(
    data=base,
    x="categoria",
    y="total",
    estimator="sum",
    errorbar=None,
    palette="Blues_d",
    ax=axes[0, 1]
)
axes[0, 1].set_title("2. Faturamento por Categoria")
axes[0, 1].set_xlabel("Categoria")
axes[0, 1].set_ylabel("Faturamento Total (R$)")

sns.barplot(
    data=base,
    x="canal",
    y="total",
    estimator="sum",
    errorbar=None,
    palette="Greens_d",
    ax=axes[1, 0]
)
axes[1, 0].set_title("3. Faturamento por Canal de Venda")
axes[1, 0].set_xlabel("Canal")
axes[1, 0].set_ylabel("Faturamento Total (R$)")

sns.countplot(
    data=base,
    x="canal",
    palette="Purples_d",
    ax=axes[1, 1]
)
axes[1, 1].set_title("4. Total de Pedidos por Canal")
axes[1, 1].set_xlabel("Canal")
axes[1, 1].set_ylabel("Quantidade de Pedidos")

# Título principal da figura
fig.suptitle("Painel de Vendas - Cafeteria Grão Certo", fontsize=15, fontweight="bold")

# Salvando a imagem antes do plt.show()
fig.savefig("painel.png", dpi=150)

# Exibindo o painel na tela
plt.show()

