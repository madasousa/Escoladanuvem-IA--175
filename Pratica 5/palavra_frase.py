"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

"""
def is_palindromo(texto) :
     texto_limpo = ''.join(char.lower())
for char in texto:
            if char.isalnum():  # Verifica se o caractere é alfanumérico
                texto_limpo += char.lower()  # Converte para minúsculo e adiciona ao texto limpo    
     
    # Remove espaços e converte para minúsculas
texto = texto.replace(" ", "").lower()

    # Verifica se o texto é igual ao seu inverso
    # texto[::-1] inverte a string
if len(texto) == 0:
     return "Sim"
else:
      if texto == texto[::-1]:
      return "Sim"
else:
    return "Não"            
print(eh_palindromo("Ame a Roma e a Roma é a mesma!"))
print(is_palindromo("Socorro, eu me enganei!"))
print(is_palindromo("Ame a Roma e a Roma é a mesma!"))
print(is_palindromo("Olá, mundo!"))
# Fim do programa


