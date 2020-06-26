temperatura_celsius = float(input("Informe a temperatura em °C: "))
temperatura_fahrenheit = (9*temperatura_celsius/5) + 32
temperatura_kelvin = temperatura_celsius + 273
print("A temperatura de {}°C corresponde a {:.1f}°F e {}K".format(temperatura_celsius, temperatura_fahrenheit, temperatura_kelvin))
