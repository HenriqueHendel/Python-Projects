#Programa que calcula quantos litros de tinta serão necessários para pintar uma área, sabendo que cada litro de tinta pinta uma área de 2m²
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura*altura
litros = area/2

print("Sua parede tem uma área de {}m². \nA quantidade de litros necessária será de {}l".format(area, litros))
