primeiro_valor = float(input("Informe o primeiro valor: "))
segundo_valor = float(input("Informe o segundo valor: "))
terceiro_valor = float(input("Informe o terceiro valor: "))

menor = primeiro_valor
if segundo_valor < primeiro_valor and segundo_valor < terceiro_valor:
    menor=segundo_valor
if terceiro_valor < segundo_valor and terceiro_valor < primeiro_valor:
    menor=terceiro_valor

maior = primeiro_valor
if segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    maior = segundo_valor
if terceiro_valor > segundo_valor and terceiro_valor > primeiro_valor:
    maior = terceiro_valor

print("O menor valor é {}".format(menor))
print("O maior valor é {}".format(maior))
