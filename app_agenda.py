#listas do contato
lista_nomes = []
lista_telefones = []

#cadastrar contato
def cadastrar_contato():
    quant = int(input('Quantidade de contatos: '))
    for i in range(quant):
        nome = input('Digite o nome do contato: ')
        lista_nomes.append(nome)
        telefone = int(input('Digite o numero: '))
        lista_telefones.append(telefone)

#listar contatos 
def listar_contatos(lista_nomes, lista_telefones):
    for i in range(len(lista_nomes)):
        print('Nome: ', lista_nomes[i])
        print('Telefone: ', lista_telefones[i])

#alterar contato
def alterar_contato():
    dado = input('Digite o nome ou numero: ')
    #dado_int = int(dado)

    for i in range(len(lista_nomes)):
        if dado == lista_nomes[i]:
            nome = input('Digite o novo nome: ')
            lista_nomes[i] = nome
            numero = int(input('Digite o novo numero: '))
            lista_telefones[i] = numero
        else:
            print('Esse contato nao existe!')


#funcao deletar
def deletar_contato():
    dado = input('Digite o nome ou numero: ')

    for i in range(len(lista_nomes)):
        if dado == lista_nomes[i]:
            lista_nomes.pop(i)
            lista_telefones.pop(i)
            print('Deletado com sucesso!')
        else:
            print('Contato nao encontrado!')

#funcao buscar
def buscar_contato():
    dado = input('Digite o nome ou numero: ')
    for i in range(len(lista_nomes)):
        if dado == lista_nomes[i]:
            print('Encontrado com sucesso!')
            print('Nome: ', lista_nomes[i])
            print('Telefone: ', lista_telefones[i])
        else:
            print('Contato nao encontrado!')
    
def menu():
    #funcao principal
    op = 1
    while op != 0:
        print('1 - Cadastrar Contato ' \
        '\n 2 - Listar Contatos ' \
        '\n 3- Alterar Contato' \
        '\n 4- Deletar Contato' \
        '\n 5- Buscar Contato' \
        '\n 0- Sair')
        op = int(input('Digite a opcao: '))
        if op == 1:
            cadastrar_contato()    
        if op == 2:
            listar_contatos(lista_nomes, lista_telefones)
        if op == 3:
            alterar_contato()
        if op == 4:
            deletar_contato()
        if op == 5:
            buscar_contato()


menu()
