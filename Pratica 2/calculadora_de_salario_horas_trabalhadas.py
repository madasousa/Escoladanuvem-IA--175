"""
Calculadora de salário por horas trabalhadas
Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. 
Calcule o salário do funcionário e exiba o resultado formatado corretamente.
Entrada:
O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando:
Número do funcionário (numero_funcionario).
Quantidade de horas trabalhadas (horas_trabalhadas).
Valor recebido por hora (valor_por_hora).

"""

# Leitura dos dados de entrada
print("Digite o número do funcionário:")
numero_funcionario = int(input())

print("Digite a quantidade de horas trabalhadas:")
horas_trabalhadas = int(input())

print("Digite o valor recebido por hora:")
valor_por_hora = float(input())

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

print("-" * 30)
print(f"Número do funcionário: {numero_funcionario}")
print(f"Salário: R$ {salario:.2f}")


