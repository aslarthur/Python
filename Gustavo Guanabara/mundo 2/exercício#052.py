#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print ('-=' * 65)
num = int(input("Digite um número: "))
print ('-=' * 65)
total = 0
for c in range (1, num + 1):
    if num % c == 0:
        print ("\033[1;3;32m", end=' ')
        total += 1
    else:
        print ("\033[31m", end=' ')
    print (f"{c}", end=' ')
if total >= 3:
    print ('-=' * 65)
    print (f"\033[1;3;35mO número {num} foi divisivel {total} vezes. Então ele\033[m\033[1;3;;31m NÃO É UM NÚMERO PRIMO\033[m")
else:
    print (f"\033[1;3;35mO número {num} foi dividido {total} vezes. Então ele \033[m\033[1;3;36mÉ UM NÚMERO PRIMO.\033[m")
    print ('-=' * 65)
