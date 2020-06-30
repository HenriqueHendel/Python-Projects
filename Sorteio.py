from random import choice
itens = input("Informe os valores que deseja sortear, seperando-os por vírgula: ")
itens = itens.split(",")
sorteado = choice(itens)
print(f"O item sorteado foi {sorteado}")
