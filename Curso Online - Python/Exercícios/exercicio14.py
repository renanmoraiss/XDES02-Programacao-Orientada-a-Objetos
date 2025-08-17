temp_celsius = float(input("Temperatura em °C: "))
temp_fahrenheit = (temp_celsius * 1.8) + 32
temp_kelvin = temp_celsius + 273.15
print("{}°C corresponde a {}°F".format(temp_celsius, temp_fahrenheit ))
print("{}°C corresponde a {} K".format(temp_celsius, temp_kelvin))