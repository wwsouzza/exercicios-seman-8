from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# 1. Definir o caminho base dinâmico
BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()

def criar_painel(base):
    # Ajusta o tema visual padrão
    sns.set_theme(style="whitegrid")

    # Prepara dados para o gráfico de entrega vs avaliação
    entrega = base.dropna(subset=["tempo_entrega_min", "avaliacao"])

    # Formata números como moeda (R$)
    reais = FuncFormatter(lambda v, pos: f"R$ {v:,.0f}".replace(",", "."))

    # Criando a estrutura de 2 linhas e 2 colunas
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 7), layout="constrained")

    # 1. Evolução Mensal do Faturamento
    sns.lineplot(
        data=base,
        x="mes",
        y="total",
        estimator="sum",
        errorbar=None,
        marker="o",
        ax=axes[0, 0]
    )
    axes[0, 0].set_title("1. Faturamento por Mês")
    axes[0, 0].set_xlabel("Mês")
    axes[0, 0].set_ylabel("Total (R$)")
    axes[0, 0].yaxis.set_major_formatter(reais)

    # 2. Faturamento por Categoria
    sns.barplot(
        data=base,
        x="categoria",
        y="total",
        estimator="sum",
        errorbar=None,
        ax=axes[0, 1]
    )
    axes[0, 1].set_title("2. Faturamento por Categoria")
    axes[0, 1].set_xlabel("Categoria")
    axes[0, 1].set_ylabel("Total (R$)")
    axes[0, 1].yaxis.set_major_formatter(reais)

    # 3. Avaliação Média por Canal de Venda
    sns.barplot(
        data=base,
        x="canal",
        y="avaliacao",
        estimator="mean",
        errorbar=None,
        ax=axes[1, 0]
    )
    axes[1, 0].set_title("3. Avaliação Média por Canal de Venda")
    axes[1, 0].set_xlabel("Canal")
    axes[1, 0].set_ylabel("Nota Média (1-5)")
    axes[1, 0].set_ylim(0, 5)

    # 4. Tempo de Entrega vs Avaliação
    sns.scatterplot(
        data=entrega,
        x="tempo_entrega_min",
        y="avaliacao",
        hue="plano",
        alpha=0.6,
        ax=axes[1, 1]
    )
    axes[1, 1].set_title("4. Tempo de Entrega vs Avaliação")
    axes[1, 1].set_xlabel("Tempo de Entrega (min)")
    axes[1, 1].set_ylabel("Nota de Avaliação")

    # Título Geral e Exportação (DENTRO da função onde fig existe)
    fig.suptitle("Painel da Grão Certo - 1º Semestre de 2025", fontsize=16, fontweight="bold")
    fig.savefig(BASE / "painel.png", dpi=150)
    print("Painel gerado e salvo como 'painel.png' com sucesso!")
    plt.show()

# Bloco de execução principal
if __name__ == "__main__":
    base = pd.read_csv(BASE / "pedidos_prontos.csv", parse_dates=["data"])
    criar_painel(base)