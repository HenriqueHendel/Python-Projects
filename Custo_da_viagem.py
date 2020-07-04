distancia = float(input("Informe a distância da sua viagem em Km: "))
if(distancia<=200):
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print("O valor da passagem para a sua viagem de {} quilômetros é de R${:.2f}.".format(distancia, passagem))