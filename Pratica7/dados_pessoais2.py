"""
Crie um script em Python que escreva dados em um arquivo CSV.
 O arquivo CSV deve conter informações pessoais,
  como colunas Nome, Idade e Cidade.
"""
import csv  
def escrever_dados_pessoas(arquivo):
    # Dados de exemplo
    pessoas = [
        {"Nome": "Alice", "Idade": 30, "Cidade": "São Paulo"},
        {"Nome": "Bob", "Idade": 25, "Cidade": "Rio de Janeiro"},
        {"Nome": "Charlie", "Idade": 35, "Cidade": "Belo Horizonte"}
    ]
    
    # Escrevendo os dados no arquivo CSV
    with open(arquivo, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Nome', 'Idade', 'Cidade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()  # Escreve o cabeçalho
        for pessoa in pessoas:
            writer.writerow(pessoa)  # Escreve cada linha de dados  
if __name__ == "__main__":
    escrever_dados_pessoas('dados_pessoais2.csv')
    print("Dados escritos com sucesso no arquivo 'dados_pessoais2.csv'.")       
# Fim do código


