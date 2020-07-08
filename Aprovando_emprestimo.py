valor_casa = float(input("Informe o valor da casa: R$ "))
valor_salario = float(input("Informe o seu salário: R$ "))
quantidade_anos=int(input("Em quantos anos pretende quitar a casa ? "))
prestacao_mensal = valor_casa/(quantidade_anos*12)
limite = valor_salario * 0.3
print("Para pagar uma casa de R$ {} em {} anos, a prestação será de R$ {:.2f}. ".format(valor_casa, quantidade_anos, prestacao_mensal), end="")
if prestacao_mensal > limite:
    print("Infelizmente não é possível realizar um empréstimo.")
else:
    print("Empréstimo Concedido.")
