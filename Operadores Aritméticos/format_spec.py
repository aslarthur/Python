# ---------------------------------------------
# EXEMPLO ORIGINAL: nome bem no meio de 20 espaços
# ---------------------------------------------
nome = input('Qual é seu nome? ')  # pergunta o nome e guarda na caixinha "nome"

print('Prazer em te conhecer {:^}!'.format(nome))
# {:=^20} -> caixa de 20 espaços, preenchida com "=", nome no MEIO
#   =  -> o que preenche o vazio (fill)
#   ^  -> centraliza (align)
#   20 -> tamanho da caixa (width)

# ---------------------------------------------

num = int(input('informe um número: '))  # pergunta um número e guarda na caixinha "num"
num1 = int(input("Informe outro número: "))
num3 = num / num1
print ('A divisão desses números é: {:.0f}'.format(num3), end= " ") #Deixa tudo em uma linha só

#Ele eliminou todas as flutuantes (números com casas decimais)

num = int(input('informe um número: '))  # pergunta um número e guarda na caixinha "num"
num1 = int(input("Informe outro número: "))
num3 = num / num1
print ('A divisão desses números  é: {:.0f}'.format(num3))
# ---------------------------------------------

# AGORA "TODAS" AS PEÇAS DO QUEBRA-CABEÇA JUNTAS
# (usando um número, pra caber sinal, casas decimais etc)
# ---------------------------------------------
valor = 1234567.891

print('{:*^+#020,.2f}'.format(valor))
# Cada pedacinho dentro do : faz UMA coisa. Bora, banana por banana:
#
#   *   -> FILL: qual símbolo enche o espaço vazio       ("usa * pra encher")
#   ^   -> ALIGN: onde o número fica                      ("centro")
#   +   -> SIGN: mostra o sinal MESMO se for positivo     ("+1.234... em vez de só 1.234...")
#   #   -> FORMA ALTERNATIVA: força detalhe extra aparecer (ex: o ponto decimal)
#   0   -> ZERO-PADDING: enche com zero grudado no sinal   (aqui perde pro fill/align manual)
#   20  -> WIDTH: tamanho TOTAL da caixa (20 quadradinhos)
#   ,   -> GROUPING: separador de milhar                   (1234567 vira 1,234,567)
#   .2  -> PRECISION: quantas casas depois da vírgula       (só 2: ".89")
#   f   -> TYPE: que "espécie" de número é                  (f = número fixo, tipo 3.14)


# ---------------------------------------------
# BANANA-GUIA RÁPIDO (só trocando o "tipo" lá no final)
# ---------------------------------------------
n_inteiro = 255
print('{:b}'.format(n_inteiro))   # b -> binário        -> 11111111
print('{:o}'.format(n_inteiro))   # o -> octal          -> 377
print('{:x}'.format(n_inteiro))   # x -> hexadecimal    -> ff
print('{:d}'.format(n_inteiro))   # d -> decimal normal -> 255

fatia = 0.25
print('{:.0%}'.format(fatia))     # % -> vira porcentagem -> 25%
