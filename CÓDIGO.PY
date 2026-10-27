def maior_palavra(lista_str):
    if not lista_str:
        return None
    maior = lista_str[0]
    for palavra in lista_str:
        if len(palavra) > len(maior):
            maior = palavra
    return maior
entrada = ["casa", "cidade", "rua", "praia", "Recife"]
print(maior_palavra(entrada))

def indices_palavras_longas(lista_str):
    longas = []
    for i in range(len(lista_str)):
        palavra_atual = lista_str[i]
        if len(palavra_atual) > 4:
            longas.append(i)
    return longas
lista_str = ["sol", "computador", "lua", "python", "casa"]
longas = indices_palavras_longas(lista_str)
print("As palavras com mais de 4 letras estão nos índices:", longas)

def palavras_com_muitos_esses(lista_str):
    esses = []
    for palavra in lista_str:
        contador = 0
        for letra in palavra:
            if letra.lower() == 's':
                contador +=1
                if contador >= 2:
                    esses.append(palavra)
    return esses
lista_str = ["casa", "passador", "salsicha", "gato", "SUCESSO"]
esses = palavras_com_muitos_esses(lista_str)
print("As palavras com 2 ou mais letras 's' são:", esses)
