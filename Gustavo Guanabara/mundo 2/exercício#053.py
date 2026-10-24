#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input("Digite uma frase: ").upper().strip().replace(" ", "")
frase_invertida = frase[::-1]
print (f"A frase {frase} invertida fica {frase_invertida}")
if frase == frase_invertida:
    print ("Temos um palindromo!")
else:
    print ("Não temos um palindromo")