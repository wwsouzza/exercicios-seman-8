from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # funciona no VS Code e no Colab

pedidos = pd.read_csv(BASE / "pedidos.csv")
produtos = pd.read_csv(BASE / "produtos.csv")
df = pedidos.merge(produtos, on="id_produto", how="left")   # dados brutos, sem limpeza

df["data"] = pd.to_datetime(df["data"])
nomes = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
df["dia"] = df["data"].dt.dayofweek.map(dict(enumerate(nomes)))
unicos = df.drop_duplicates()
bom = df[df["tempo_entrega_min"] < 120]

pasta = BASE / "graficos1"
pasta.mkdir(exist_ok=True)
sns.set_theme(style="whitegrid")

# 1) Histograma do tempo de entrega, com os extremos
plt.figure(figsize=(5, 3.6))
sns.histplot(df["tempo_entrega_min"].dropna(), bins=20)
plt.title("Tempo de entrega (com extremos)")
plt.savefig(pasta / "tempo_com_extremos.png", dpi=120)
plt.close()
# obs1: concentrado perto de 30 min, com um possivel outlier em 480.
#faria: verificação do valor 480


# 2) Histograma abaixo de 120 minutos
plt.figure(figsize=(5, 3.6))
sns.histplot(bom["tempo_entrega_min"], bins=15)
plt.title("Tempo de entrega (abaixo de 120 min)")
plt.savefig(pasta / "tempo_sem_extremos.png", dpi=120)
plt.close()



# 3) Boxplot da quantidade por categoria
plt.figure(figsize=(5, 3.6))
sns.boxplot(data=df, x="categoria", y="qtd")
plt.title("Quantidade por categoria")
plt.savefig(pasta / "boxplot_qtd.png", dpi=120)
plt.close()
# Obs1: pedidos com 40 unidades em todas as categorias 
# faria: verificar possivel erro de digitação.

# 4) Pedidos por dia da semana (sem duplicados)
plt.figure(figsize=(5, 3.6))
sns.countplot(data=unicos, x="dia", order=nomes)
plt.title("Pedidos por dia da semana")
plt.savefig(pasta / "pedidos_por_dia.png", dpi=120)
plt.close()
# Obs1: sexta e fim de semana aumentam as vendas
# faria: ações para o fim de semana e promoções para os dias da semana.

print("Gráficos gravados em:", pasta)
for arquivo in sorted(pasta.glob("*.png")):
    print(" -", arquivo.name)
