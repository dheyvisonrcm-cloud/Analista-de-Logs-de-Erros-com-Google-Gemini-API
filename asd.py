def calcula_dobro(n):
    return n * 2
resultado = calcula_dobro(5)
print(resultado)

def verificar_maior(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
verificar_maior(10,6)


def pode_sacar(saldo_atual, valor_saque):
    if saldo_atual >= valor_saque:
        return saldo_atual - valor_saque
    else:
        return "saldo insuficiente"
    
pode_sacar(100, 50)
resultado = pode_sacar(100, 50)
print(resultado)

def classificar_triangulo(l1,l2,l3):
    if l1 == l2  == l3:
        return "equilátero"
    elif l1 != l2 or l1 != l3 or l2 != l3 and l1 == l2 or l1 == l3 or l2 == l3:
        return "isósceles"
    else:
        return "escaleno"
classificar_triangulo(3, 4, 5)
resultado = classificar_triangulo(3, 4, 5)
print(resultado)

def calcula_imposto(n):
    if n <= 2000:
        return 0
    elif 2000 < n < 5000:
        return n *0.10
    else:
        return n * 0.20
calcula_imposto(2300)
resultado = calcula_imposto(2300)
print(resultado)

