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
            
estudantes=[]
estudantes=pedir(estudantes)
arquivo="arquivo.txt"
escrever(estudantes, arquivo)
mostrar(arquivo)
