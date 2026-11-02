from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()
pedidos = pd.read_csv(BASE / "pedidos.csv")
produtos = pd.read_csv(BASE / "produtos.csv")
df = pedidos.merge(produtos, on="id_produto", how="left")

pasta = BASE / "graficos1"
pasta.mkdir(exist_ok=True)
sns.set_theme(style="whitegrid")

print("== 1. Tamanho e tipos ==")
print(df.shape)
print(df.dtypes.to_string())

print("\n== 2. Ausentes e duplicados ==")
tabela = pd.DataFrame({"nulos": df.isna().sum(), "pct": (df.isna().mean() * 100).round(1)})
print(tabela[tabela["nulos"] > 0])
print(df.duplicated().sum(), "linhas duplicadas")

print("\n== 3. Categorias ==")
print(df["canal"].nunique(), "grafias de canal")
print(df["canal"].value_counts().head(3))
df["data"] = pd.to_datetime(df["data"])
df["canal"] = df["canal"].str.strip().str.title()
df["total"] = df["qtd"] * df["preco"]
df["mes"] = df["data"].dt.month
df["dia_semana"] = df["data"].dt.dayofweek
nomes = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
df["dia"] = df["dia_semana"].map(dict(enumerate(nomes)))
print("Canais depois:", df["canal"].nunique())


print("\n== 4. Números ==")
print(df[["qtd", "avaliacao", "tempo_entrega_min", "preco"]].describe().round(1))
t = df["tempo_entrega_min"].dropna()
q1, q3 = t.quantile([0.25, 0.75])
limite = q3 + 1.5 * (q3 - q1)
print(f"Regra do IQR: limite {limite:.1f} min | {(df['tempo_entrega_min'] > limite).sum()} pedidos acima")
plt.figure(figsize=(5, 3.6))
sns.boxplot(data=df, x="categoria", y="qtd")
plt.title("Quantidade por categoria")
plt.savefig(pasta / "boxplot_qtd.png", dpi=120)
plt.close()
bom = df[df["tempo_entrega_min"] < 120]
plt.figure(figsize=(5, 3.6))
sns.histplot(bom["tempo_entrega_min"], bins=15)
plt.title("Tempo de entrega (abaixo de 120 min)")
plt.savefig(pasta / "histograma_tempo.png", dpi=120)
plt.close()


print("\n== 5. Tempo ==")
unicos = df.drop_duplicates()
print(unicos["dia"].value_counts().reindex(nomes).to_string())
por_mes = unicos.groupby(["mes", "categoria"]).size().unstack()
print(por_mes)
plt.figure(figsize=(5, 3.6))
por_mes.plot(marker="o")
plt.ylabel("pedidos")
plt.title("Pedidos por categoria e mês")
plt.savefig(pasta / "pedidos_por_mes.png", dpi=120)
plt.close()


print("\n== 6. Relações ==")
cols = ["qtd", "avaliacao", "tempo_entrega_min", "total"]
r1 = df["tempo_entrega_min"].corr(df["avaliacao"])
r2 = bom["tempo_entrega_min"].corr(bom["avaliacao"])
print(f"Correlação tempo x nota: com os 480 min {r1:.2f} | sem eles {r2:.2f}")
plt.figure(figsize=(5, 3.6))
sns.heatmap(bom[cols].corr(), annot=True, cmap="Greens", vmin=-1, vmax=1)
plt.title("Correlações (tempo abaixo de 120 min)")
plt.savefig(pasta / "heatmap_correlacoes.png", dpi=120, bbox_inches="tight")
plt.close()


