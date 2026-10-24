while True:
    try: 
        numero = int(input("Digite um número: "))
        resultado = 10 / numero
    except Exception as erro:
        print (f"Erro: {erro}")
        continue
    else:
        print (f"{numero} / 10 = {resultado}")
        break
