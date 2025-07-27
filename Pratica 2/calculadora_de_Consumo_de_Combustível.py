"""
Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo.
Use os seguintes dados:
Distância percorrida: 300 km
Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, 
incluindo o resultado final arredondado para duas casas decimais.

"""
# Dados da viagem
distancia_percorrida = 300  # em km
combustivel_gasto = 25  # em litros

# Cálculo do consumo médio
consumo_medio = distancia_percorrida / combustivel_gasto  # em km/l

consumo_medio_arredondado = round(consumo_medio, 2)  # arredondando para duas casas decimais

# Exibição dos resultados
print("Dados da Viagem:")
print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print("-" * 30)
print(f"Consumo médio: {consumo_medio_arredondado} km/l")
