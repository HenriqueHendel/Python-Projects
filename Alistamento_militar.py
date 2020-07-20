sexo = int(input("Informe 1 para sexo masculino ou 2 para feminino: "))
if sexo == 1:
    from datetime import date
    ano_nascimento = int(input("Informe o ano de nascimento: "))
    ano_atual = date.today().year
    idade =  ano_atual - ano_nascimento
    if idade < 18:
        anos_para_alistar = 18-idade
        ano_de_alistamento = ano_atual + anos_para_alistar
        print("Atualmente você tem {} anos".format(idade))
        print("Seu alistamento será daqui a {} ano(s), ou seja, em {}".format(anos_para_alistar, ano_de_alistamento))
    elif idade == 18:
        print("Você deve se alistar esse ano.")
    elif idade > 18:
        ano_de_alistamento = ano_atual - (idade-18)
        print("Seu ano de alistamento foi em {}. Caso não tenha se alistado, procure a junta militar mais próxima para "
              "resolver sua situação.".format(ano_de_alistamento))
else:
    print("Você não precisa se alistar.")
