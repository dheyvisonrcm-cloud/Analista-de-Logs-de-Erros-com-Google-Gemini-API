

def indices_muitas_vogais(lista_str, n):
    resultado = []
    vogais = 'aeiouAEIOU'
    for i in range(len(lista_str)):
        palavra_atual = lista_str[i]
        contador_vogais = 0
        for letra in palavra_atual:
            if letra in vogais:
                contador_vogais += 1
        if contador_vogais > n:
            resultado.append(i)
    return resultado
lista_str = ["marcas", "uva", "abacaxi", "café", "zebra", "pepino"]
n = 2
resultado = indices_muitas_vogais(lista_str, n)
print ("As palavras com mais de", n, "vogais estão nos índices:", resultado)

def menor_palavra_ultimo(lista_str):
    menor = lista_str[0]
    for palavra in lista_str:
        if len(palavra) <= len(menor):
            menor = palavra
    return menor
lista_str = ["casa", "sol", "lua", "mar"]
menor = menor_palavra_ultimo(lista_str)
print(f"A menor palavra da lista é: {menor}")

def palavras_pares(lista_str):
    palavra_par = []
    for palavra in lista_str:
        if len(palavra) % 2 == 0:
            palavra_par.append(palavra)
    return palavra_par
lista_str = ["casa", "uva", "abacaxi", "sol"]
palavra_par = palavras_pares(lista_str)
print("As palavras com número par de letras são:", palavra_par)

def começa_com_vogal(lista_str):
    palavras_vogais = []
    for palavra in lista_str:
        if palavra[0] in 'aeiouAEIOU':
            palavras_vogais.append(palavra)
    return palavras_vogais
lista_str = ["abacaxi", "sol", "elefante", "rua", "Igreja"]
palavras_vogais = começa_com_vogal(lista_str)
print("As palavras que começam com vogal são:", palavras_vogais)

def conta_letra_na_lista(lista_str, letra_alvo):
    contador = 0
    for palavra in lista_str:
        for letra in palavra:
            if letra.lower() == letra_alvo.lower():
                contador += 1
    return contador
lista_str = ["casa", "abacaxi", "sol"]
letra_alvo = "a"
contador = conta_letra_na_lista(lista_str, letra_alvo)
print ("O número de vezes que a letra 'a' aparece na lista é:", contador)

def limpa_negativos(lista_num):
    nova_lista = []
    for n in lista_num:
        if n < 0:
            n = 0
            nova_lista.append(n)
        else:
            nova_lista.append(n)
    return nova_lista

lista_num = [2, -5, 10, -1, 0, -8]
nova_lista = limpa_negativos(lista_num)
print(f"sua nova lista é: {limpa_negativos(lista_num)}")

def posicao_da_palavra_longa(lista_str):
    palavra_maior = []
    for i in range(len(lista_str)):
        if len(lista_str[i]) > 6:
            palavra_maior.append(i)
            return i
    return -1
lista_str = ["sol", "casa", "python", "computador", "lua", "abacaxi"]
palavra_maior = posicao_da_palavra_longa(lista_str)
print("a posição da maior palavra é:", palavra_maior)

def possui_numero_par(lista_num):
    for n in lista_num:
        if n % 2 == 0:
            return True
    return False
lista_num = [1, 3, 5, 8, 9]

def possui_numero_par(lista_num):
    for n in lista_num:
        if n % 2 == 0:
            return True
    return False
lista_num = [1, 3, 5, 7]


def classifica_textos(lista_str):
    maior = 0
    menor = 0
    for palavra in lista_str:
        if len(palavra) > 5:
            maior += 1
        elif len(palavra) < 4:
            menor += 1
    return maior, menor
lista_str = ["sol", "casa", "python", "rio", "abacaxi", "trem"]
quantidade_maior, quantidade_menor = classifica_textos(lista_str)
print("sua quantidade de palavras menores de 4 letras é", quantidade_menor)
print("sua quantidade de palavras maiores de 5 letras é", quantidade_maior)

def fatorial_dos_positivos(lista_num):
    contador = 1
    for n in lista_num:
        if n > 0 :
            contador = contador * n
    return contador
lista_num = [2, -3, 3, -1, 4]
contador = fatorial_dos_positivos(lista_num)
print(f"o fatorial dessa lista, ignorando os negativos é:, {fatorial_dos_positivos(lista_num)}")

def contar_palavras_com_letras_repetidas(lista_str):
    contador = 0
    for palavra in lista_str:
        if len(palavra) > 2 and palavra[0].lower() == palavra[-1].lower():
            contador += 1
            
    return contador
lista_str = ["Arara", "sol", "ovo", "casa", "o"]
contador = contar_palavras_com_letras_repetidas(lista_str)
print(f"a lista de palavras que começa com a mesma letra e termina com a mesma letra é, {contar_palavras_com_letras_repetidas(lista_str)}")

def produto_dos_pares_em_posicoes_impares(lista_num):
    contador = 1
    for i in range(len(lista_num)):
        if i % 2 != 0:
            contador = contador * n
    return contador ##ERRADOOOOOOO, tem que pegar um número DENTRO da lista
lista_num = [4, 6, 3, 4, 9, 2]
contador = produto_dos_pares_em_posicoes_impares(lista_num)
print (f"sua multiplicação é, {produto_dos_pares_em_posicoes_impares(lista_num)}")

def produto_dos_pares_em_posicoes_impares(lista_num):
    contador = 1
    for i in range(len(lista_num)):
        numero_atual = lista_num[i] #QUANDO VOCÊ QUER PEGAR UM NÚMERO DENTRO DO I, PRIMEIRO VOCÊ DEFINE QUE O NUMERO DEVE SER TRATADO COMO UM
        if i % 2 != 0 and numero_atual % 2 == 0:
            contador = contador * numero_atual
    return contador
lista_num = [4, 6, 3, 4, 9, 2]
contador = produto_dos_pares_em_posicoes_impares(lista_num)
print (f"sua multiplicação é, {produto_dos_pares_em_posicoes_impares(lista_num)}")

def contem_senha_valida(lista_str):
    numero = "1234567890"
    for palavra in lista_str:   
        if len(palavra) > 6 and palavra in numero:
            return True
        else:
            return False # ERRADDOOOOOOOO, ele assim só iria parar na primeira
        
def contem_senha_valida(lista_str):
    numero = "1234567890"
    for palavra in lista_str:
        if len(palavra) > 6:
            for caractere in palavra:
                if caractere in numero:
                    return True
    return False

def maior_palavra(lista_str):
    maior = ""
    for palavra in lista_str:
        if len(palavra) > len(maior):
            maior = palavra
    return maior
lista_str = ["casa", "cidade", "rua", "praia", "Recife"]
maior = maior_palavra(lista_str)
print(f"sua maior palavra é, {maior_palavra(lista_str)}")

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
