""""
Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais).

"""
# idade = int(input("Digite a sua idade: "))
idade = int(input("Digite a sua idade: "))
if idade < 0:
    print("Idade inválida. Por favor, insira uma idade não negativa.")  
elif idade <= 12:
    print("Você é uma Criança.")
elif idade <= 17:
    print("Você é um Adolescente.")
elif idade <= 59:
    print("Você é um Adulto.")
elif idade >= 60:
    print("Você é um Idoso.")
else:
    print("Idade inválida. Por favor, insira uma idade válida.")
# Fim do programa
