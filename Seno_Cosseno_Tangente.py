from math import radians, sin, cos, tan
angulo = float(input("Informe um ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O seno de {} equivale a {:.2f}".format(angulo, seno))
print("O cosseno de {} equivale a {:.2f}".format(angulo, cosseno))
print("A tangente de {} equivale a {:.2f}".format(angulo, tangente))
