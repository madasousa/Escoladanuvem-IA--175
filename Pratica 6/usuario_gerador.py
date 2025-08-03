"""
Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
O programa deve exibir o nome, email e país do usuário gerado.

"""

import requests

# Função para gerar um perfil de usuário aleatório
def gerar_perfil_usuario():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        user_info = data['results'][0]
        
        nome = f"{user_info['name']['first']} {user_info['name']['last']}"
        email = user_info['email']
        pais = user_info['location']['country']
        
        return {
            'nome': nome,
            'email': email,
            'pais': pais
        }
    else:
        return None

# Função principal
def main():
    print("Gerador de Perfil de Usuário Aleatório")
    perfil = gerar_perfil_usuario()
    
    if perfil:
        print(f"Nome: {perfil['nome']}")
        print(f"E-mail: {perfil['email']}")
        print(f"País: {perfil['pais']}")
    else:
        print("Erro ao gerar o perfil do usuário.") 

if __name__ == "__main__":
    main()
    

