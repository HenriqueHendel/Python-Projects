#Programa que calcula o valor de um produto com X% de desconto
valor_produto = float(input("Digite o Valor do Produto em reais: "))
desconto = int(input("Digite o Valor do desconto em porcentagem: "))

valor_com_desconto = valor_produto - valor_produto*(desconto/100);

print("O produto com {}% de desconto fica com o valor de R${:.2f}".format(desconto, valor_com_desconto))
