#Calculando a hipotenusa sabendo os catetos
from math import pow, sqrt, hypot
cateto_oposto = float(input("Informe o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Informe o comprimento do cateto adjacente: "))
'''hipotenusa = hypot(cateto_oposto, cateto_adjacente)'''
soma_catetos = pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)
hipotenusa = sqrt(soma_catetos)
print("A hipotenusa vai medir {:.2f}".format(hipotenusa))
