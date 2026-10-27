
print ("gasolina vs álcool")
resposta = input("está pronto para começar?").lower()
if resposta == "sim":
    try:
        gasolina = float(input("digite o preço da gasolina:"))
        if gasolina <= 0:
            print(("preço da gasolina inválido, por favor digite um valor maior que zero."))
            gasolina = float(input("digite o preço da gasolina:"))
            if gasolina <= 0:
                print ("preço da gasolina inválido, por favor digite um valor maior que zero.")
            while True:
                gasolina = float(input("digite o preço da gasolina:"))
                if gasolina <= 0:
                        print ("preço da gasolina inválido, por favor digite um valor maior que zero.")
                        continue
                else:
                        break
        elif gasolina > 0:
            pass
    except ValueError:
        print(("entrada inválida, por favor digite um número."))
        while True:
            try:
                gasolina = float(input("digite o preço da gasolina:"))
                if gasolina <= 0:
                    print ("preço da gasolina inválido, por favor digite um valor maior que zero.")
                    continue
                else:
                    break
            except ValueError:
                print ("entrada inválida, por favor digite um número.")
                continue
    try:
        álcool = float(input("digite o preço do álcool:"))
        if álcool <= 0:
            print(("preço do álcool inválido, por favor digite um valor maior que zero."))
            álcool = float(input("digite o preço do álcool:"))
            if álcool <= 0:
                print ("preço do álcool inválido, por favor digite um valor maior que zero.")
                while True:
                    álcool = float(input("digite o preço do álcool:"))
                    if álcool <= 0:
                        print ("preço do álcool inválido, por favor digite um valor maior que zero.")
                        continue
                    else:
                        break
        elif álcool > 0:
         pass    

    except ValueError:
        print ("entrada inválida, por favor digite um número.")
        while True:
            try:
                álcool = float(input("digite o preço do álcool:"))
                if álcool <= 0:
                    print ("preço do álcool inválido, por favor digite um valor maior que zero.")
                    continue
                else:
                    break
            except ValueError:
                print ("entrada inválida, por favor digite um número.")
                continue

    
    resultado = álcool / gasolina
    if resultado <= 0.7:
        print ("o álcool é mais vantajoso")
    elif resultado > 0.7:
        print ("a gasolina é mais vantajosa")
    resposta = input ("gostaria de realizar uma nova comparação? digite sim para continuar ou não para sair:")
    if resposta == "sim":
            while True:
                gasolina = float(input("digite o preço da gasolina:"))
                if gasolina <= 0:
                    print ("preço da gasolina inválido, por favor digite um valor maior que zero.")
                    continue
                else:
                    break
    elif resposta == "não":
            print ("ok")
    elif resposta != "sim" and resposta != "não":
            print ("resposta inválida:")
            resposta = input ("por favor digite sim ou não:")
            if resposta == "sim":
             while True:
               gasolina = float(input("digite o preço da gasolina:"))
               if gasolina <= 0:
                print ("preço da gasolina inválido, por favor digite um valor maior que zero.")
                continue
               else:
                break

elif resposta.lower() == "não":
    print ("tchau")
    exit()
elif resposta.lower() != "sim" and resposta.lower() != "não":
    print ("resposta inválida, por favor digite sim ou não.")
    resposta = input("está pronto para começar?")
    if resposta.lower() == "sim":
        while True:
            gasolina = float(input("digite o preço da gasolina:"))
            if gasolina <= 0:
                print ("preço da gasolina inválido, por favor digite um valor maior que zero.")
                continue
            else:
                break
    elif resposta.lower() == "não":
        print ("tchau")
        exit()