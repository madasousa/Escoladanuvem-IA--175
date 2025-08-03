"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. 
O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.

"""
import requests

# Função para consultar o endereço pelo CEP
def consultar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        endereco = response.json()
        if 'erro' not in endereco:
            return endereco
        else:
            return f"none: CEP {cep} não encontrado"
    else:
        return f"None: Erro ao consultar o CEP {cep}. Status code: {response.status_code}"   
    
    print("Bem-vindo ao consultador de endereços por CEP!")
# Função principal
def main():
    cep = input("Digite o CEP que deseja consultar: ").strip()
    
    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido. Certifique-se de que o CEP possui 8 dígitos numéricos.")
        return
    
    endereco = consultar_endereco(cep)
    
    if isinstance(endereco, dict):
        print(f"Logradouro: {endereco.get('logradouro')}")
        print(f"Bairro: {endereco.get('bairro')}")
        print(f"Cidade: {endereco.get('localidade')}")
        print(f"Estado: {endereco.get('uf')}")
    else:
        print(endereco)

if __name__ == "__main__":
    main()
            



