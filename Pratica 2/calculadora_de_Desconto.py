"""
Calculadora de Desconto 
Desenvolva um programa que calcula o desconto em uma loja.
Use as seguintes informações:
Nome do produto: "Camiseta"
Preço original: R$ 50.00
Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final
"""
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Cálculo do valor do desconto
valor_desconto = (porcentagem_desconto / 100) * preco_original

# Cálculo do preço final
preco_final = preco_original - valor_desconto

# Exibição dos resultados
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Porcentagem de desconto: {porcentagem_desconto}%")
print("-" * 30)
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
# Fim do programa
print("-" * 30)