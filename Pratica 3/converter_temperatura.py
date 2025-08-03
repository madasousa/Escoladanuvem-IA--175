"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
O programa deve exibir o resultado da conversão.

"""

# Função para converter Celsius para Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Função para converter Celsius para Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Função para converter Fahrenheit para Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função para converter Fahrenheit para Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

# Função para converter Kelvin para Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Função para converter Kelvin para Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Função principal para realizar a conversão
def converter_temperatura():

    temperatura = float(input("Informe a temperatura: "))
    unidade_origem = input("Informe a unidade de origem (Celsius, Fahrenheit, Kelvin): ").strip().lower()
    unidade_destino = input("Informe a unidade de destino (Celsius, Fahrenheit, Kelvin): ").strip().lower()

    if unidade_origem == "celsius":
        if unidade_destino == "fahrenheit":
            resultado = celsius_to_fahrenheit(temperatura)
            print(f"{temperatura} °C é igual a {resultado} °F")
        elif unidade_destino == "kelvin":
            resultado = celsius_to_kelvin(temperatura)
            print(f"{temperatura} °C é igual a {resultado} K")
        else:
            print("Unidade de destino inválida.")
    
    elif unidade_origem == "fahrenheit":
        if unidade_destino == "celsius":
            resultado = fahrenheit_to_celsius(temperatura)
            print(f"{temperatura} °F é igual a {resultado} °C")
        elif unidade_destino == "kelvin":
            resultado = fahrenheit_to_kelvin(temperatura)
            print(f"{temperatura} °F é igual a {resultado} K")
        else:
            print("Unidade de destino inválida.")
    
    elif unidade_origem == "kelvin":
        if unidade_destino == "celsius":
            resultado = kelvin_to_celsius(temperatura)
            print(f"{temperatura} K é igual a {resultado} °C")
        elif unidade_destino == "fahrenheit":
            resultado = kelvin_to_fahrenheit(temperatura)
            print(f"{temperatura} K é igual a {resultado} °F")
        else:
            print("Unidade de destino inválida.")
    
    else:
        print("Unidade de origem inválida.")        

# Executa a função principal
if __name__ == "__main__":
    converter_temperatura()

# Fim do código