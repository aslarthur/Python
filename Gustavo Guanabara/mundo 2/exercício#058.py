# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
def l():
    print ('-=' * 65)
tentativas = 0 
escolhido = randint(0, 11)
l()
print ("\033[1;3;32mPensando em um número...\033[m")
l()
sleep (3.00)
print ("\033[1;3;33mPensei!\033[m")
l()
numero_do_user = int(input("Tente adivinhar o número que pensei: "))
l()
print ("\033[1;3;35mVERIFICANDO...\033[m")
sleep (3.00)
l()
while numero_do_user != escolhido:
    if numero_do_user > escolhido:
        print ("\033[1;3;4;36mMenor!\033[m")
        l()
        numero_do_user = int(input("Tente novamente: "))
    else:
        print ("\033[1;3;4;34mMaior!\033[m")
        l()
        numero_do_user = int(input("Tente novamente: "))
        
    l()
    print ("\033[1;3;4;35mVERIFICANDO...\033[m")
    sleep (3.00)
    l()
    tentativas += 1

print ("\033[1;3;32mVocê acertou!\033[m")
l()
if tentativas > 0:
    print (f"Você precisou de {tentativas + 1} tentativas para acertar!")
    
else:
    print (f"Você precisou de {tentativas + 1 } tentativa para acertar!")
l()