def celsiusParaFahrenheit(temp_celsius): #função que retorna a temperatura em Fahrenheit
    temp_fahrenheit = (temp_celsius * 1.8) + 32
    return temp_fahrenheit

def fahrenheitParaCelsius(temp_fahrenheit): #função que retorna a temperatura em Celsius
    temp_celsius = (temp_fahrenheit - 32) * 1.8
    return temp_celsius

celsius = float(input("Temperatura em Celsius: "))
fahrenheit = float(input("Temperatura em Fahrenheit: "))

#chamando as funções
conversaoParaFahrenheit = celsiusParaFahrenheit(celsius)
conversaoParaCelsius = fahrenheitParaCelsius(fahrenheit)

print("{} Grau Celsius = {} Grau Fahrenheit".format(celsius, conversaoParaFahrenheit))
print("{} Grau Fahrenheit = {} Grau Celsius".format(fahrenheit, conversaoParaCelsius))