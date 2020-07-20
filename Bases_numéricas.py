numero = int(input("Digite um número inteiro: "))
print("Escolha para qual base deseja converter: ")
print("[ 1 ] BINÁRIO")
print("[ 2 ] OCTADECIMAL")
print("[ 3 ] HEXADECIMAL")
base = int(input("Sua escolha: "))
if base == 1:
    print("{} convertido para binário é igual a {}".format(numero, bin(numero)[2:]))
elif base == 2:
    print("{} convertido para octadecimal é igual a {}".format(numero, oct(numero)[2:]))
elif base == 3:
    print("{} convertido para hexadecimal é igual a {}".format(numero, hex(numero)[2:]))
else:
    print("O número {} não representa uma base disponível, tente novamente.".format(base))

