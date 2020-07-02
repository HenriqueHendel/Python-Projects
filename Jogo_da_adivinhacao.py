from random import randint
print("Vou pensar em um número de 0 a 5. Tende adivinhar...")
print("-=-"*20)
numero_usuario = int(input("Em que número eu pensei:"))
numero_selecionado = randint(0, 5)
print("Processando...")
if(numero_usuario==numero_selecionado):
    print("Você acertou! O número que eu pensei foi {}!".format(numero_selecionado))
else:
    print("Ganhei! Eu pensei no número {} e não no {}!".format(numero_selecionado, numero_usuario))
