def pedir(estudantes):
    dicionario={}
    while True:
        nome=input("digite o nome do estudante(digite sair para encerrar):")
        if nome=="sair":
            break
        idade=int(input("digite a idade"))
        curso=input("digite o curso:")
        dicionario={"nome": nome,"idade": idade, "curso": curso}
        estudantes.append(dicionario)
    return estudantes

def escrever(estudantes, arquivo):
    with open(arquivo, "w")as arquivo:
        for estudante in estudantes:
            arquivo.write(f"nome:{estudante['nome']}")
            arquivo.write(f"idade:{estudante['idade']}")
            arquivo.write(f"curso:{estudante['curso']}")

def mostrar(arquivo):
    with open(arquivo, "r")as arquivo:
        for linha in arquivo:
            print(linha)

def atualizar(arquivo, estudantes):
    nome=input("digite o nome para atualizar:")
    for estudante in estudantes:
        if estudante["nome"]==nome:
            r=input("digite se deseja atualizar o nome, idade ou curso:")
            if r=="nome":
                estudante["nome"]=input("digite o novo nome:")
            elif r=="idade":
                estudante["idade"]=input("digite a nova idade:")
            elif r=="curso":
                estudante["curso"]=input("digite o novo curso:")
        else:
            print("o estudante não existe")
    with open(arquivo, "w")as arquivo:
        for estudante in estudantes:
            arquivo.write(f"nome:{estudante['nome']}")
            arquivo.write(f"idade:{estudante['idade']}")
            arquivo.write(f"curso:{estudante['curso']}")

def informar(arquivo):
    nome=input("digite o nome do estudante:")
    dicionario={}
    with open(arquivo, "r")as arquivo:
        for linha in arquivo:
            chave, valor = linha.strip().split(': ')
            if valor==nome:
                print(f"{chave}:{valor}")

def opcao(estudantes, arquivo):
    while True:
        r=int(input(("digite 1 para adicionar estudantes, 2 paraver o arquivo, 3 para atualizar, 4 para ver informações do aluno, 0 para encerrar:")))
        if r==1:
            estudantes=pedir(estudantes)
        elif r==2:
            mostrar(arquivo)
        elif r==3:
            arquivo=atualizar(arquivo, estudantes)
        elif r==3:
            informar(arquivo)
        elif r==0:
            break

estudantes=[]
arquivo="arquivo.txt"
arquivo=escrever(estudantes, arquivo)
opcao(estudantes, arquivo)
