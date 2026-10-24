# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input("Digite quanto você pesa em KG: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
print (f"O IMC dessa pessoa é de {imc:.1f}")
if imc <= 18.5:
    print ("Você está abaixo do PESO NORMAL")
elif 18.5 < imc  <= 25:
    print ("PARABÉNS! Você está na faixa de PESO IDEAL")
elif 26 < imc <= 30:
    print ("Você está em SOBREBESO, Cuidado!")
elif 30 < imc <= 40:
    print ("Obesidade")
else:
    print ("Você está em OBESIDADE MÓRBIDA, Cuidado!")