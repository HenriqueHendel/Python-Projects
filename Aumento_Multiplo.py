salario = float(input("Informe o salário do funcionário: "))
if salario > 1250:
    salario = salario + salario * 0.1
else:
    salario = salario + salario * 0.15
print("O novo salário do funcionário é de R${:.2f}".format(salario))
