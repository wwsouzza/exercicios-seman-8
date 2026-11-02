# Registro de Problemas encontrados:
Problema Quantos  Decisão sugerida
Linhas duplicadas 12 Remover com drop_duplicates()
Quantidade inválida (-1 ou 40) 7 Investigar com o negócio; excluir da análise de faturamento
Tempo de entrega de 480 min 3 Tratar como nulo se for código de erro
Delivery sem tempo 6 Manter e avisar que faltam dados
Pedido sem cliente 128 Manter: são vendas de balcão não identificadas
Pedido sem avaliação 116 Manter; não imputar a nota
Canal com 9 grafias 9 → 3 Corrigir com .str.strip().str.title()


# Achados relacionados ao negócio:

1. Quedas nas vendas do produto Café, com o passar do tempo ( caiu de 80 em Janeiro para 28 em Junho)
2. Concetração de pedidos nas sextas, sabados e domingos.
3. Tem um pico de um pedido de 40 em quantidade.

# Possiveis ações a serem feitas:

1. Buscar entender porque a queda nas vendas do produto café.
2. Refazer escalas de trabalho para suportar os picos de fim de semana.
3. Verificar se o pedido de 40 é real ou erro de digitação. 