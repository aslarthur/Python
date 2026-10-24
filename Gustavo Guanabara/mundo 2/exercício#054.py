#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date 
i = 0 
n = 0
ano_atual = date.today().year
for a in range (1, 8):
    ano_de_nascimento = int(input(f"Digite o {n + 1}ª ano de nascimento: "))
    idade = ano_atual - ano_de_nascimento
    if idade <= 17:
        i += 1
    else:
        n += 1

print (f"{i} pessoas não atingiram a maioridade!")
print (f"{n} pessoas atingiram a maioridade!")