# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

# * A média de idade do grupo.


# * Qual é o nome do homem mais velho.


# * Quantas mulheres têm menos de 20 anos.

somaidade = 0
media = 0
maioridadedohomem = 0
nomedomaisvelho = ''
totalmulher20 = 0
for n in range (1, 5):
    print ("{:-^20}".format (f" {n}ª PESSOA "))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F]: ")).strip()
    somaidade += idade
    if n == 1 and sexo in "Mn":
        maioridadedohomem = idade
        nomedomaisvelho = nome
    if sexo in "Mn" and idade > maioridadedohomem:
        maioridadedohomem = idade
        nomedomaisvelho = nome
    if sexo in "Ff" and idade < 20:
        totalmulher20 += 1
media = somaidade / 4
print (f"A média de idade do grupo é de {media} anos")
print (f"O homem mais velho tem {maioridadedohomem} e se chama {nomedomaisvelho}")
print (f"Ao todo são {totalmulher20} mulheres com menos de 20 anos")