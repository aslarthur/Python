# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nova_nota1 = float(input("Digite a primeira nota: "))
nova_nota2 = float(input("Digite a segunda nota: "))
nota = (nova_nota1 + nova_nota2) / 2
print (f"Tirando {nova_nota1:.1f} e {nova_nota2:.1f} a média do aluno é {nota:.1f}")
if nota < 5:
    print ("REPROVADO")
elif nota >=7:
    print ("APROVADO!")
else:
    print ("RECUPERAÇÃO")
