"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro  (BRL). 
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, 
máximo e mínimo da cotação, além da data e hora da última atualização. 
Utilize a API da AwesomeAPI para obter os dados de cotação

"""
import requests

# Função para consultar a cotação da moeda
def consultar_cotacao(moeda):   
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)
    
    if response.status_code == 200:
        cotacao = response.json()
        if moeda in cotacao:
            return cotacao[moeda]
        else:
            return f"none: Moeda {moeda} não encontrada"
    else:
        return f"None: Erro ao consultar a moeda {moeda}. Status code: {response.status_code}"  
    
    print("Bem-vindo ao consultador de cotações de moedas!")
# Função principal      
def main():
    moeda = input("Digite o código da moeda que deseja consultar (ex: USD, EUR, GBP): ").strip().upper()
    
    if not moeda.isalpha() or len(moeda) < 3:
        print("Código de moeda inválido. Certifique-se de que o código possui pelo menos 3 letras.")
        return
    
    cotacao = consultar_cotacao(moeda)
    
    if isinstance(cotacao, dict):
        print(f"Cotação atual: {cotacao.get('bid')}")
        print(f"Valor máximo: {cotacao.get('high')}")
  USD      print(f"Valor mínimo: {cotacao.get('low')}")
print(f"Data e hora da última atualização: {cotacao.get('create_date')}")
else:
print(cotacao)

if __name__ == "__main__":
    main()

        print(f"Valor mínimo: {cotacao.get('low')}")
        print(f"Data e hora da última atualização: {cotacao.get('create_date')}")
    else:
        print(cotacao)
    

