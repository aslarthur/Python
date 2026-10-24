#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print ('''Suas opções:
0. Pedra
1. Papel
2. Tesoura''')
jogada = int(input("Digite o número da sua jogada: "))
print ("-=" * 15)
sleep (1)
print ("JO")
sleep (1)
print ("KEN")
sleep (1)
print ("PO!")

print (f"Computador jogou {itens[computador]}")
print (f"Jogador jogou {itens[jogada]}")
print ("-=" * 15)

if computador == 0:

    if jogada == 0:
        print ("EMPATE")
    elif jogada == 1:
        print ("O jogador GANHOU!")
    elif jogada == 2:
        print ("O computador GANHOU!")
    else:
        print ("Opção inválida!")
elif computador == 1:
        
    if jogada == 0:
        print ("O computador GANHOU!")
    elif jogada == 1:
        print ("EMPATE")
    elif jogada == 2:
        print ("O jogador GANHOU!")
    else:
        print ("Opção inválida!")

elif computador == 2:

    if jogada == 0:
        print ("O jogador GANHOU")
    elif jogada == 1:
        print ("O computador GANHOU")
    elif jogada == 2:
        print ("EMPATE")
    else:
        print ("Opção inválida!")