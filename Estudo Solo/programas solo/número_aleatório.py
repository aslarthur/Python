def l():
    print ("-=" * 65)
def e():
    print()
cores = {'Branco': '\033[1;3;4;37m', 
         'Vermelho':'\033[1;3;4;31m',
         'Verde': '\033[1;3;4;32m',
         'Amarelo': '\033[1;3;4;33m',
         'Azul': '\033[1;3;4;34m',
         'Roxo': '\033[1;3;4;35m',
         'Azul claro': '\033[1;3;4;36m',
         'Cinza': '\033[1;3;4;30m'
        }
parar = '\033[m'
l()
while True:
    print (f"{cores['Roxo']}Bem vindo ao Tente adivinhar qual é!{parar}")
    l()
    print ("Digite um número de 1 a 100:")
    l()
    from random import choice
    numeros = set(range(1, 101))
    numero_escolhido = choice(list(numeros))
    while True:
        try:
            
            num1 = int(input("Digite um número: "))
            l()
            if num1 < 1 or num1 >100 :
                raise Exception(f"{cores ['Vermelho']}Digite um número válido!{parar}")
            break
        except Exception as erro:
            
            print (f"Erro: {erro}")
            l()


    if num1 > numero_escolhido:
        print (f"{cores ['Azul']}Menor!{parar}")
    elif num1 < numero_escolhido:
        print (f"{cores ['Verde']}Maior!{parar}")
    else:
        print (f"{cores ['Amarelo']}Você ganhou de mim!{parar} ")
        break
    l()
    while True:
        try:
            print ("Deseja continuar?")
            l()
            print ("1. Sim")
            l()
            print ("2. Não")
            l()
            sn = input("Digite o número ou a sua resposta aqui: ").upper().strip()
            
            if sn not in ("SIM", "NÃO", "1", "2"):
                raise Exception("Digite uma resposta válida!")

        except Exception as erro:
            print (f"Erro: {erro}")
        
        if sn == "2" or sn == "NÃO":
            l()
            print ("Tudo bem!")
            l()
            break
        elif sn == "1" or sn == "SIM":
            l()
            print ("Ótimo!")
            l()
            break
    if sn == "2" or sn == "NÃO":
        break