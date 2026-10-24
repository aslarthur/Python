#Faça um programa que faça a soma de todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
soma = 0
cont = 0
for n in range (1, 501):
    if n % 3 == 0 and n % 2 != 0:
        soma += n
        cont += 1
print ("A soma dos valores que notal é de {} é de: {}".format (cont, soma))