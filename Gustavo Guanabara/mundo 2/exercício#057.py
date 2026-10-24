# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input("Digite seu sexo [M/F]: ").upper().strip()[0]
while sexo not in ("M", "F"):
    print ("Resposta incorreta! Tente novamente.")
    sexo = input("Digite seu sexo [M/F]: ").upper().strip()[0]
if sexo in "M":
    print ("Sexo masculino registrado com sucesso")
else:
    print ("Sexo feminino registrado com sucesso")