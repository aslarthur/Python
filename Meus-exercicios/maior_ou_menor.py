quantidade = maior = menor = 0
sn = "S"
while sn == "S":
    while True:
        try:
            num = int(input("Digite um número: "))
            break
        except ValueError as erro:
            print (f"Erro: {erro}")
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    while True:
        try:
            sn = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
            if sn not in ("S", "N"):
                raise IndexError ("Digite algo válido! ")
            break
        except IndexError as erro:
            print (f"Erro: {erro}")
        
print (f"O maior número: {maior}")
print (f"O menor: {menor}")