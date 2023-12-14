def adicionar(compras):
    dicionario={}
    while True:
        produto=input("digite o nome do produto(digite sair para encerrar):")
        if produto=="sair":
            break
        valor=float(input("digite o preço:"))
        dicionario={produto: valor}
        compras.append(dicionario)
    return compras

def adicionar_arquivo(compras, arq_compras):
    with open(arq_compras, "w")as arquivo:
        for compra in compras:
            arquivo.write(compra)

def atualizar(compras, arq_compras):
    produto_at=input("digite a compra que quer atualizar o preço:")
    for compra in compras:
        for produto, valor in compra.items():
            if produto == produto_at:
                compra[produto]=float(input("digite o novo preço:"))
    with open(arq_compras, "w")as arquivo:
        for compra in compras:
            arquivo.write(compra)
    return compras, arq_compras

def preco_total(compras):
    precos=[]
    for compra in compras:
        for produto, valor in compra.items():
            if valor not in precos:
                precos.append(valor)
    total=sum(precos)
    print("o preço total é de {total} reais")

def opcao(arq_compras, compras):
    while True:
        r=int(input("digite 1 para adicionar uma compra, 2 para atualizar o preço, 3 para ver o preço total, 0 para encerrar:"))
        if r==1:
            compras=adicionar(compras)
        elif r==2:
            compras, arq_compras=atualizar(compras, arq_compras)
        elif r==3:
            preco_total(compras)
        elif r==0:
            break

compras=[]
arq_compras="arquivo.txt"
arq_compras=adicionar_arquivo(arq_compras, compras)
opcao(arq_compras, compras)
