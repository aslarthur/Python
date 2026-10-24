# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
def e():
    print ()
def l():
    print ("-=" * 65)


l()
n1 = int(input("Digite um número: "))
l()
n2 = int(input("Digite outro número: "))
from time import sleep
l()
sleep (2)

while True:
    
    palavra = "Opções"
    cores = [37, 31, 32, 33, 34, 35, 36, 30]
    for i, (a) in enumerate (palavra):
        print (f"\033[1;3;4;{cores[i]}m{a}\033[m", end="")
    print (": ")
    e()
    print ("[1] somar")
    print ("[2] multiplicar")
    print ("[3] maior")
    print ("[4] novos números")
    print ("[5] sair do programa")
    e()
    opcao = int(input("Digite o número da opção aqui: "))
    l()
    if opcao == 1:
        print (f"{n1} + {n2} = {n1 + n2}")
        
    elif opcao == 2:
        print (f"{n1} x {n2} = {n1 * n2}")
       
    elif opcao == 3:
        if n1 > n2:
            print (f"O maior entre {n1} e {n2} é {n1} ")
        elif n1 < n2:
            print (f"O maior entre {n1} e {n2} é {n2}")
        else:
            print (f"Os números {n1} e {n2} são iguais.")            
        
    elif opcao == 4:
        n1 = int(input("Digite um número: "))
        
        n2 = int(input("Digite outro número: "))
    elif opcao == 5:
        print ("\033[1;3;37mFinalizando...\033[m")
        l()
        sleep(2)
        print ("\033[1;3mSaindo... Até logo! 👋\033[m")
        l()
        break
    else:
        print ("Opção não encontrada! Tente novamente.")
