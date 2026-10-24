# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num_para_parar = 999
soma_do_total = 0
contador_de_quantos_numeros = 0
num = int(input('Digite um número [999 para parar]: '))
while num != num_para_parar:
    soma_do_total += num
    contador_de_quantos_numeros += 1
    num = int(input("Digite outro número [999 para parar]: "))  
    
print (f"Soma total: {soma_do_total}")
print (f"Foram digitados: {contador_de_quantos_numeros} números")
print ("Acabou!")
