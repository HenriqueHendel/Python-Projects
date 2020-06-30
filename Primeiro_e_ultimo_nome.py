frase = str(input("Digite seu nome completo: ")).strip()
primeiro_espaco = frase.find(" ")
ultimo_espaço = frase.rfind(" ")
primeiro_nome = frase[:primeiro_espaco]
último_nome = frase[ultimo_espaço+1:]
print("Prazer em te conhecer!")
print("Seu primeiro nome é \"{}\"".format(primeiro_nome))
print("Seu último nome é \"{}\"".format(último_nome))
