# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print ("{:=^40}".format (" Lojas Arthur "))

preco = float(input("Digite o valor do produto: "))
valor = int(input(f'''
O valor do produto é de R${preco:.2f}. Formas de pagamento:
1. A vista no dinheiro/cheque: 10 % de desconto
2. A vista no cartão: 5 % de desconto
3. Em até 2x no cartão: preço normal
4. 3x ou mais no cartão: 20 % de juros
Digite o número da forma de pagamento: '''))
if valor == 1:
    preco1 = preco - (preco * 10 / 100 )
    print (f"O valor total da sua compra de R${preco:.2f} é de R${preco1:.2f}")
elif valor == 2:
    preco1 = preco - (preco * 5 / 100)
    print (f"O valor total da sua compra de R${preco:.2f} é de R${preco1:.2f}")
elif valor == 3:
    print (f"O valor total é de R${preco:.2f}")
elif valor == 4:
    preco1 = preco + (preco * 20 / 100)
    meses = int(input("Em quantas parcelas? "))
    parcela = preco1 / meses 
    
    print (f"A parcela de R${preco:.2f} em {meses}x é de R${parcela:.2f} COM JUROS")
    print (f"O valor total da sua compra de R${preco:.2f} é de R${preco1:.2f}")
else:
    print ("Opção inválida!")