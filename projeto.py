lista_de_tarefas = []

def adicionar():
    nome = input("Digite o nome da tarefa: ")
    categoria = input("Digite a categoria da tarefa: ")
    prioridade = input("Digite a prioridade da tarefa: ")
    status = input("Digite o status da tarefa: ")
    print("Tarefa cadastrada.")
    nova_tarefa = {
    "Nome": nome,
    "Categoria": categoria,
    "Prioridade": prioridade,
    "Status": status
    }
    lista_de_tarefas.append(nova_tarefa)

def concluir():
    concluir = input("Digite o nome da tarefa que você quer concluir: ")
    qtde_tarefas_concluidas = 0
    for element in lista_de_tarefas:
        if element["Nome"] == concluir.lower():
            element["Status"] = "Concluída."
            qtde_tarefas_concluidas += 1
            print("Status da tarefa atualizado para concluída.")
        if qtde_tarefas_concluidas == 0:
            print("Tarefa não encontrada.")

def prioridade():
    prioridade = input("Digite a prioridade das tarefas que você quer ver: ")
    lista_de_prioridade = []
    for element in lista_de_tarefas:
        if prioridade.lower() == element['Prioridade']:
            lista_de_prioridade.append(element)
            print(lista_de_prioridade)

def categoria():
    categoria = input("Digite a prioridade das tarefas que você quer ver: ")
    lista_de_categoria = []
    for element in lista_de_tarefas:
        if categoria.lower() == element['Categoria']:
            lista_de_categoria.append(element)
            print(lista_de_categoria)

def remover():
    remover = input("Digite o nome da tarefa que você quer remover: ")
    qtde_tarefas_removidas = 0
    for element in lista_de_tarefas:
        if element["Nome"] == remover:
            lista_de_tarefas.remove(element)
            qtde_tarefas_removidas += 1
            print("Tarefa removida com sucesso")
        if qtde_tarefas_removidas == 0:
            print("Tarefa não encontrada")

while True:
    menu = input("""
    Escolha uma opção:
    1 - Adicionar tarefa
    2 - Ver todas as tarefas
    3 - Concluir uma tarefa
    4 - Filtrar tarefas por prioridade
    5 - Filtrar tarefas por categoria
    6 - Remover uma tarefa
    0 - Sair
""")
    if menu == "1":
        n = int(input("Quantas tarefas? "))
        for i in range(n):
            adicionar()
    elif menu == "2":
        for element in lista_de_tarefas:
            print(f"""
                  Nome: {element['Nome']}
                  Categoria: {element['Categoria']}
                  Prioridade: {element['Prioridade']}
                  Status: {element['Status']}
""")
    elif menu == "3":
        concluir()
    elif menu == "4":
        prioridade()
    elif menu == "5":
        categoria()
    elif menu == "6":
        remover()
    elif menu == "0":
        break