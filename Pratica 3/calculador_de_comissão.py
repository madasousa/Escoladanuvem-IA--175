"""
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 

Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e
montante total das vendas efetuadas por este vendedor, respectivamente. 

Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

"""
#nome_vendedor = input("Digite o nome do vendedor: ")
nome_vendedor = input().strip()
salario_fixo = float(input())
total_vendas = float(input())
comissao = total_vendas * 0.15
total_a_receber = salario_fixo + comissao

print(f"TOTAL = R$ {total_a_receber:.2f}")
# Exemplo de uso:
# nome_vendedor = "João"
# salario_fixo = 5000.00    
# total_vendas = 1230.50
# comissao = total_vendas * 0.15
# total_a_receber = salario_fixo + comissao
# print(f"TOTAL = R$ {total_a_receber:.2f}")
## Saída esperada:
# TOTAL = R$ 5854.57
# Exemplo de uso:
# nome_vendedor = "Maria"   
# salario_fixo = 3000.00
# total_vendas = 1500.00
# comissao = total_vendas * 0.15
# total_a_receber = salario_fixo + comissao
# print(f"TOTAL = R$ {total_a_receber:.2f}")
# Saída esperada:
# TOTAL = R$ 3225.00



