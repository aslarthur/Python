def l():
    print ('-=' * 50)
def e():
    print ()
total = 0 
cores = {"Branco": "\033[1;3;4;37m", 
         "Vermelho": "\033[1;3;4;31m", 
         "Verde": "\033[1;3;4;32m", 
         "Amarelo": "\033[1;3;4;33m", 
         "Azul": "\033[1;3;4;34m", 
         "Roxo": "\033[1;3;4;35m", 
         "Azul claro": "\033[1;3;4;36m", 
         "Cinza": "\033[1;3;4;30m"
        }
parar = "\033[m"
nome = "Art Café"
saldo = 200
l()
print (f"{cores ["Roxo"]}Bem vindo a cafeteria {nome}{parar}")
while True:
    l()
    e()
    palavra = "Produtos"
    cores_numeros = [37, 31, 32, 33, 34, 35, 36, 30]
    for i, (n) in enumerate(palavra):
        print (f"\033[1;3;4;{cores_numeros[i]}m{n}\033[m", end="")
    print (" :")
    e()
    produtos = {"Café": 5.62, 
                "Café com leite": 7.13, 
                "Pão na chapa": 9.12, 
                "Pão de queijo": 7.31
            }
    for i, (a, b) in enumerate(produtos.items(), start = 1):
        print (f"{i}. {a} R${b}")
    e()
    l()
    while True:
        try:
            
            produto_desejado = str(input("Digite o número ou produto que deseja: ")).upper().strip()
            l()
            if produto_desejado not in ("1", "2", "3", "4", "CAFÉ", "CAFÉ COM LEITE", "PÃO NA CHAPA", "PÃO DE QUEIJO"):
                raise Exception(f"{cores["Vermelho"]}Digite algo válido!{parar}")
            break
        except Exception as erro:
            
            print (f"Erro: {erro}")
            l()
    while True:
        try:
            quantidade = int(input("Digite a quandidade do produto que deseja: "))
            numeros = set(range(1, 51))
            if quantidade not in numeros:
                
                raise Exception("Digite uma quantidade válida!")
            break
        except Exception as erro:
            l()
            print (f"{cores["Vermelho"]}Erro: {erro}{parar}")
            l()
    if produto_desejado == "1" or produto_desejado == "CAFÉ":
        total = produtos['Café'] * quantidade
    elif produto_desejado == "2" or produto_desejado == "CAFÉ COM LEITE":
        total = produtos['Café com leite'] * quantidade
    elif produto_desejado == "3" or produto_desejado == "PÃO NA CHAPA":
        total = produtos['Pão na chapa'] * quantidade
    elif produto_desejado == "4" or produto_desejado == "PÃO DE QUEIJO":
        total = produtos['Pão de queijo'] * quantidade
    l()
    
    print (f"Saldo inicial: {saldo:.2f}")
    l()
    print (f"Compra: {total:.2f}")
    l()
    
    if total <= saldo:
        saldo -= total
        print (f"Novo saldo: {saldo:.2f}")
    else:
        print ("Você não pode fazer essa compra!")
    l()
    print ("Deseja continuar?")
    l()
    print ("1. Sim")
    l()
    print ("2. Não")
    l()
    while True:
        try:
            sn = str(input("Digite o número ou a resposta aqui: ")).upper().strip()
            if sn not in ("1", "2", "SIM", "NÃO"):
                raise Exception("Digite algo válido!")
            break
        except Exception as erro:
            l()
            print (f"Erro: {cores['Vermelho']}{erro}{parar}")
    if sn == "1" or sn == "SIM":
        l()
        print ("Ótimo!")
       
    elif sn == "2" or sn == "NÃO":
        l()
        print ("Tudo bem!")
        l()
        break

    