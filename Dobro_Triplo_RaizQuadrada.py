from math import sqrt
valor = float(input("Informe um número: "))
dobro = valor*2
triplo = valor*3
raiz = valor**(1/2) or sqrt(valor)

print("O dobro de {} é {}".format(valor, dobro))
print(f"O triplo de {valor} é {triplo}")
print("A raiz quadrada de", valor, "é", raiz)
