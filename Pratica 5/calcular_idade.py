"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""
# Solicita o ano de nascimento
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Solicita o ano atual
ano_atual = int(input("Digite o ano atual: "))

# Calcula a idade em anos
idade_anos = ano_atual - ano_nascimento

# Converte a idade em anos para dias (considerando 365 dias por ano)
idade_dias = idade_anos * 365

# Exibe a idade em dias
print(f"A idade em dias é: {idade_dias} dias")
# Fim do programa
