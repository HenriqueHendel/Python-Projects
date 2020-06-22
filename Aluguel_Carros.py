#Calculando o valor do aluguel de um veículo de acordo com Km rodados e número de dias, sabendo que cada dia equivale a 60 reais e cada Km 0.15 centavos
dias = int(input("Por quantos dias o automóvel foi alugado: "))
quilometros = float(input(("Qual a quilometragem percorrida: ")))

valor_aluguel = (dias*60) + (0.15*quilometros)

print("O total do aluguel é de R${:.2f}".format(valor_aluguel))
