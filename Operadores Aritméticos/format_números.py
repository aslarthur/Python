n1 = int(input("Escreve um valor ai mané: "))
n2 = int(input("Boa, agora escreve outro: "))

a = n1 + n2
b = n1 * n2 
c = n1 / n2 
d = n1 - n2 
e = n1 // n2 
f = n1 ** n2

print (f"O resultado em adição é {a}")
print (f"O resultado em mulplicação é {b}")
print (f"O resultado em divisão é {c}")
print (f"O resultado em subtração é {d}")
print (f"O resultado em divisão inteira é {e}")
print (f"O resultado em esponenciação é {f}")

# _____________________________________________________

n3 = int(input("Digite um valor: "))
n4 = int(input("Digite outro valor: "))

g = n3  +  n4
h = n3  -  n4
i = n3  *  n4
j = n3  /  n4 
k = n3  // n4
l = n3  ** n4

print ("O resultado em adição é : {:.0f}".format (g))
print ("O resultado em subtração é : {:.0f}".format (h))
print ("O resultado em multiplicação é: {:.0f}". format (i))
print ("O resultado em divisão é: {:.0f}".format (j))
print ("O resultado em divisão inteira é: {:.0f}".format (k))
print ("O resultado em potenciação é: {:.0F} ".format (l))