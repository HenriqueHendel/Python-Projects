velocidade = float(input("Informe a velocidade atual do carro: "))
if(velocidade<=80):
    print("Tenha um bom dia! Diriga com segurança")
else:
    multa = (velocidade-80) * 7
    print("Multado! Você excedeu o limite permitido de 80km/h.")
    print("Você deve pagar uma multa de R$ {}".format(multa))
    print("Tenha um bom dia! Diriga com segurança!")
