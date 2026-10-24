#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print (f"\033[1;3;36m{"=":=^50}\033[m")
print (f"\033[1;3;32;4m10 TERMOS DE UMA PA\033[m")
print (f"\033[1;3;36m{"=":=^50}\033[m")
n0 = int(input("Digite o primeiro termo: "))
print (f"\033[1;3;36m{"=":=^50}\033[m")
r = int(input("Digite a razão: "))
print (f"\033[1;3;36m{"=":=^50}\033[m")
for c in range (0, 10):
    n0 += r
    print (f"{n0 - r} →", end=" ")

print (f"\033[1;3;4;33mACABOU\033[m")
print (f"\033[1;3;36m{"=":=^50}\033[m")