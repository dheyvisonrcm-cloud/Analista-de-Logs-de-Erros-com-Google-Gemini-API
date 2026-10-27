
convidados = []
while True:
    nome = input("qual o seu nome?").lower()
    if nome != "fim":
        convidados.append(nome)
    elif nome == "fim":
        break
print ("Lista de convidados: ", convidados) #mas porque só fica perguntando o nome e não mostra nada?

def calcula_media():
    valores = []
    while True:
        n = int(input("Digite um número (ou -1 para sair): "))
        if n < 0:
            break
        elif n >= 0:
            valores.append(n)
soma = sum(valores)

print ("A média dos valores digitados é:", soma/ len(valores))