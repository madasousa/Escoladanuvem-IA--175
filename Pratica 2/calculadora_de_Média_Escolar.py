"""
Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. 
Use as seguintes notas:
Nota 1: 7.5
Nota 2: 8.0
Nota 3: 6.5 
O programa deve calcular a média e exibir todas as notas e o resultado final,
arredondando para duas casas decimais.
"""
# Definindo as 
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# Calculando a média
media = (nota1 + nota2 + nota3) / 3
media_arredondada = round(media, 2) 

print(f"nota 1: {nota1:.1f}")
print(f"nota 2: {nota2:.1f}")
print(f"nota 3: {nota3:.1f}")
print("-" * 30)
print(f"Média: {media_arredondada:.2f}")
