"""
Crie um programa que solicite ao usuário que insira números inteiros. 
O programa deve continuar solicitando números até que o usuário digite 'fim'.
Para cada número inserido, o programa deve informar se é par ou ímpar. 
Se o usuário inserir algo que não seja um número inteiro, 
o programa deve informar o erro e continuar.
No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.

"""

# Inicialização de contadores
contagem_pares = 0
contagem_impares = 0

white True:
    # Solicita ao usuário que insira números inteiros
    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
        
        if entrada.lower() == 'fim':
            break
        
        try:
            numero = int(entrada)
            
            # Verifica se o número é par ou ímpar
            if numero % 2 == 0:
                print(f"{numero} é par.")
                contagem_pares += 1
            else:
                print(f"{numero} é ímpar.")
                contagem_impares += 1
                
        except ValueError:
            print("Erro: Por favor, insira um número inteiro válido.")
# Exibe a contagem de números pares e ímpares
print(f"Números pares: {contagem_pares}")
print(f"Números ímpares: {contagem_impares}")
# Adicionando funcionalidade para calcular a média das notas
