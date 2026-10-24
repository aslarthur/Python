# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = 1
total = 0 
mais = 10
pausas = 0
while mais != 0:
    total += mais
    while contador <= total:
        print (f"{termo} - ", end="")
        termo += razao
        contador += 1
    print ("PAUSA")
    pausas += 1
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print (f"Progressão finalizada com {total} termos")