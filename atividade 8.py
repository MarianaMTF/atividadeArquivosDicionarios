def adicionar(contatos):
    dicionario={}
    nome=input("digite o nome do contato:")
    numero=int(input("digite o numero do contato:"))
    dicionario={"contato": nome, "numero": numero}
    contatos.append(dicionario)
    return contatos

def adicionar_arquivo(arquivo_ct, contatos):
    with open(arquivo_ct, "w")as arquivo:
        for contato in contatos:
            arquivo.write(f"contato:{contato['contato']}")
            arquivo.write(f"numero:{contato['numero']}")
    return arquivo_ct

def visualizar(arquivo_ct):
    with open(arquivo_ct, "r")as arquivo:
        for linha in arquivo:
            print(linha)

def atualizar(contatos, arquivo_ct):
    nome=input("Digite o nome do contato:")
    for contato in contatos:
        if nome==contato["nome"]:
            r=input("digite se deseja atualizar o nome ou o numero:")
            if r=="nome":
                nome_at=input("digite o novo nome:")
                contato["nome"]=nome_at
            elif r=="numero":
                numero_at=int(input('digite o novo numero:'))
                contato["numero"]=numero_at
        else:
            print('o nome não esta no arquivo')
    with open (arquivo_ct, "w") as arquivo:
        for contato in contatos:
            arquivo.write(f"nome:{contato['nome']}")
            arquivo.write(f"numero:{contato['numero']}")
    return contatos, arquivo_ct

def remover(contatos, arquivo_ct):
    nome=input("digite o nome que deseja remover:")
    for contato in contatos:
        if contato["nome"]==nome:
            contatos.remove(contato)
        else:
            print("o contato não esta no arquivo")
    with open(arquivo_ct, "w")as arquivo:
        for contato in contatos:
            arquivo.write(f"nome:{contato['nome']}")
            arquivo.write(f"numero:{contato['numero']}")
    return contatos, arquivo_ct

def opcao(arquivo_ct):
    while True:
        r=int(input("digite 1 para adicionar um novo contato, 2 para visualizar, 3 para atualizar, 4 para excluir um contato, 0 para encerrar o programa:"))
        if r==1:
            contatos=adicionar(contatos)
        elif r==2:
            visualizar(arquivo_ct)
        elif r==3:
            contatos, arquivo_ct=atualizar(contatos, arquivo_ct)
        elif r==4:
            contatos, rquivo_ct=remover(contatos, rquivo_ct)
        
contatos=[]
arquivo_ct="arquivo.txt"
arquivo_ct=adicionar_arquivo(arquivo_ct, contatos)
opcao(arquivo_ct, contatos)
