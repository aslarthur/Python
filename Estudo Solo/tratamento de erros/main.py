# try:
#     n1 = int(input("Digite um número: "))
#     n2 = int(input("Digite outro número: "))
#     resultado = n1 + n2
#     print (f"A soma entre {n1} e {n2} é {resultado}")
# except Exception as erro:
#     print (f"Erro: {erro}")
#     print ("Digite um número válido!")

# print ("Fim do código")

# try: 
#     numero = float(input("Digite um número: "))
#     resultado = 10 / numero
#     print (f"O resultado é {resultado}")
# except ValueError as erro:
#     print (f"Erro: {erro}")
# except ZeroDivisionError as erro:
#     print (f"Erro: {erro}")

# try:
#     frutas = ["Maçã", "Pera", "Banana"]
#     print (frutas[3])
# except IndexError as erro:
#     print (f"Erro ocorrido: {erro}")

# try: 
#     numero = float(input("Digite um número: "))
#     resultado = 10 / numero

# except ValueError as erro:
#     print (f"Erro: {erro}")
# except ZeroDivisionError as erro:
#     print (f"Erro: {erro}")
# else:
#     print (f"O resultado é {resultado}")
# finally:
#     print ("Fim do cáuculo ")

try:
    idade = int(input("Digite sua idade: "))
    if idade <0:
        raise ValueError ("Digite uma idade válida! ")
except Exception as erro:
    print (f"Erro: {erro}")
else:
    print (f"Sua idade é: {idade}")