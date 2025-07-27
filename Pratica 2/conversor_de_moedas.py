"""Conversor de moeda
Criar um programa que converte um valor em reais para dólares e euros.
Use os seguintes dados:
Valor em reais: R$ 100.00
Taxa do dólar: R$ 5.60
Taxa do euro: R$ 6.60
"""
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

# Conversão de reais para dólares
valor_dolares = valor_reais / taxa_dolar
valor_dolares_arredondado = round(valor_dolares, 2)

# Conversão de reais para euros
valor_euros = valor_reais / taxa_euro
valor_euros_arredondado = round(valor_euros, 2)

# Exibição dos resultados
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Valor em dólares: $ {valor_dolares_arredondado:.2f}")
print(f"Valor em euros: € {valor_euros_arredondado:.2f}")
print("-" * 30)
print(f"Valor convertido em dolares: US$ {valor_dolares_arredondado:.2f}")
print(f"Valor convertido em euros: € {valor_euros_arredondado:.2f}")

