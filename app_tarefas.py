
#lista globais
lista_nomes = []
lista_status = []
lista_data_cad = []
lista_data_lim = []

def cadastrar_tarefa():
    quant = int(input('Digite quantas taferas voce deseja:'))
    for i in range(quant):
        nome = input('Digite o nome da tarefa:')
        lista_nomes.append(nome)
        status = int(input('Digite 1- OK e 0- Off: '))
        lista_status.append(status)
        data_cad = input('Data de cadastro Ex. 10/07/25: ')
        lista_data_cad.append(data_cad)
        data_lim = input('Data de limite Ex. 10/07/25: ')
        lista_data_lim.append(data_lim)
        print()

def listar_tarefas(listanome,listastatus,listalim):
    for i in range(len(listanome)):
        print('Tarefa: ', listanome[i])
        print('Status', listastatus[i])
        print('Data limite: ', listalim[i])
        print()

#alterar tarefas
def alterar_taraefa(listanome,listastatus,listalim):
    info = input('Digite o nome da tarefa: ')
    for i in range(len(listanome)):
        if info == listanome[i]: 
            nome = input('Digite o nome da tarefa:')
            lista_nomes[i] = nome
            status = int(input('Digite 1- OK e 0- Off: '))
            lista_status[i] = status
            data_cad = input('Data de cadastro Ex. 10/07/25: ')
            lista_data_cad[i] = data_cad
            data_lim = input('Data de limite Ex. 10/07/25: ')
            lista_data_lim[i] = data_lim
            print()
        else:
            print('Tarefa nao encontrada!')

#fucao deletar tarefa
def deletar_tarefa(listanomes):
    info = input('Digite o nome da tarefa que deseja deletar: ')
    for i in range(len(listanomes)):
        if info == listanomes[i]:
            lista_nomes.pop(i)
            lista_status.pop(i)
            lista_data_cad.pop(i)
            lista_data_lim.pop(i)
            print('Tarefa deletada com sucesso!')
        else:
            print('Tarefa nao encontrada!')


def buscar_tarefas(listanome):
    info = input('Digite o nome da tarefa: ')
    for i in range(len(listanome)):
        if info == listanome[i]:
            print('Tarefa: ', lista_nomes[i])
            print('Status', lista_status[i])
            print('Data limite: ', lista_data_lim[i])
            print()
        else:
            print('Tarefa nao encontrada!')


def menu():
    op = 1
    while op != 0:
        print('1 - Cadastrar Tafera')
        print('2 - Listar Tarefas')
        print('3 - Alterar Tarefas')
        print('4 - Deletar Tarefas')
        print('5 - Buscar Tarefas')
        print('0 - Sair')

        op = int(input('Digite a opcao: '))
        if op == 1:
            cadastrar_tarefa()
        if op == 2: 
            listar_tarefas(lista_nomes,lista_status,lista_data_lim)
        if op == 3:
            alterar_taraefa(lista_nomes)
        if op == 4:
            deletar_tarefa(lista_nomes)
        if op == 5:
            buscar_tarefas(lista_nomes)
        
menu()