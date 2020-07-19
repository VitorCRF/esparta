listaAtividades = ["Ler", "Escrever", "Estudar", "Assistir", "Caminhar"] #Variaveis criadas e populadas com exemplos
listaPendentes = ["Escrever", "Caminhar"]
listaFinalizadas = ["Ler", "Estudar", "Assistir"]
#-------------------------------------------------------------------------------------------------------------------------
#Funções com as funcionalidades
def adicionaTarefa(tarefa):
    listaAtividades.append(tarefa) #Adiciona a tarefa na lista de atividades
    listaPendentes.append(tarefa) #Adiciona a tarefa na lista de atividades pendentes
    print("Tarefa adicionada com sucesso!")
    return tarefa


def finalizaTarefa(finaliza):
    if finaliza > len(listaAtividades): #Verifica se o número de entrada confere com alguma tarefa
        print("Tarefa não encontrada, tente outra vez.")
    else: #Caso seja compatível, o código é executado
        print(f'A tarefa {finaliza} foi finalizada com sucesso!')
        confirma = input("Deseja desfazer essa ação? S / N: ") #Fornece ao usuário a opção de desfazer a ação
        if confirma in "Ss": #Verifica se o usuário digitou S ou s para desfazer a ação
            print("Ação desfeita!")
        elif confirma in "Nn": #Caso a entrada seja N ou n a ação é confirmada e a tarefa é finalizada
            listaFinalizadas.append(listaPendentes[finaliza]) #Adiciona a tarefa ao final da lista de tarefas finalizadas
            listaPendentes.remove(listaPendentes[finaliza]) #Remove a tarefa da lista de tarefas pendentes
            print(f"A tarefa {finaliza} foi finalizada!") #Mostra ao usuário o número da tarefa que foi finalizada.
        else: #Se o valor de entrada não for compatível com nenhuma tarefa a mensagem abaixo será exibida
            print("Entrada inválida, tente outra vez!")
    return finaliza


def listaAtividadesPendentes():
    i = int(0) #Variável utilizada como contador
    print('-' * 139) #Traços de separação utilizada apenas por estética do programa
    print("Essas são as suas tarefas pendentes")
    print('-' * 139)
    while i < len(listaPendentes): #Percorre toda a lista de tarefas pendentes
        print(f'{i}. {listaPendentes[i]}') #Imprime na tela o número e o nome da tarefa
        i = i + 1 #Variável de contador é incrementada em 1
    print('-' * 139)

    return listaPendentes


def listaAtividadesFinalizadas():
    i = int(0)
    print("Essas são as suas tarefas finalizadas")
    while i < len(listaFinalizadas):
        print(f'{i}. {listaFinalizadas[i]}')
        i = i + 1
    return listaFinalizadas


def removeAtividade(remover):
    if remover > len(listaAtividades) or remover < 0: #Verifica se a entrada do usuário é compatível com alguma tarefa
        print("Tarefa não encontrada, tente outra vez.")
    else: #Caso seja compatível, o código abaixo será executado
        confirm = input("Tem certeza que deseja excluir a tarefa? S/N ") #Pede a confirmação do usuário para excluir a tarefa
        if confirm in "Ss": #Caso confirmado, o código abaixo será executado
            pos = listaAtividades[remover] #Variável utilizada para receber o nome da tarefa
            listaAtividades.remove(listaAtividades[remover]) #Remove a tarefa através da entrada do usuário
            if pos in listaPendentes: #Se o nome da tarefa estiver presente na lista de tarefa pendentes, ela também deverá ser removida
                indice = listaPendentes.index(pos) #Variável criada para receber o índice em que essa tarefa se encontra na lista de tarefas pendentes
                listaPendentes.remove(listaPendentes[indice]) #Encontrado o índice, é feita a remoção da atividade
            if pos in listaFinalizadas: #Verifica se a tarefa está entre as finalizadas
                indice = listaFinalizadas.index(pos)
                listaFinalizadas.remove(listaFinalizadas[indice]) #Caso esteja, será feita a remoção da mesma através do seu índice
            print(f'Atividade {remover} removida com sucesso!')
        elif confirm in "Nn": #Caso o usuário não confirme, a mensagem abaixo será exibida
            print("Tarefa não removida!")
    return remover
#-------------------------------------------------------------------------------------------------------
print('-' * 139)
#Verifica se a lista possui alguma tarefa ou está vazia
if len(listaAtividades) <= 0:
    print("Sua lista de tarefas ainda está vazia, adicione alguma no menu abaixo")
else:
    print("Essa é a sua lista de tarefas:")
    for i in range(len(listaAtividades)):
        print(f'{i}.', listaAtividades[i])
    print('-' * 139)
#--------------------------------------------------------------------------------------------------------
#Loop infinito para execução do código
while True:
    menu = int(input("Digite 1 para abrir o menu de opções ou 0 para encerrar o programa: ")) #Entrada para execução ou não do menu
    if menu == 1: #Verifica se o menu deve ser exibido
        print('Adicionar uma nova atividade tecle 1\nPara finalizar uma atividade tecle 2\nPara verificar as atividades pendentes tecle 3\nPara verificar as atividades finalizadas tecle 4\nPara remover uma atividade tecle 5\nPara verificar todas as atividades tecle 6')
    elif menu == 0: #Finaliza o programa
        print("Programa finalizado com sucesso!")
        break
    else:
        print("Comando inválido, tente outra vez!")
    verificar = int(input("Digite aqui: ")) #Verifica o que o usuário deseja fazer
    if verificar == 1:
        adicionaTarefa(input("Informe a tarefa a ser adicionada: ")) #Chama a função que irá executar o código
    elif verificar == 2:
        i = int(0)
        print('Essas são as suas tarefas pendentes')
        while i < len(listaPendentes):
            print(f'{i}. {listaPendentes[i]}')
            i = i + 1
        finaliza = finalizaTarefa(int(input("Informe o numero da tarefa que deseja finalizar: ")))

    elif verificar == 3:
        listaAtividadesPendentes()
    elif verificar == 4:
        listaAtividadesFinalizadas()
    elif verificar == 5:
        i = int(0)
        while i < len(listaAtividades):
            print(f'{i}. {listaAtividades[i]}')
            i = i + 1
        remover = removeAtividade(int(input('Digite o número da atividade que deseja excluir: ')))

    elif verificar == 6:
        if len(listaAtividades) <= 0:
            print("Sua lista de tarefas ainda está vazia, adicione alguma no menu abaixo")
        else:
            print('-' * 139)
            print("Essa é a sua lista de tarefas:")
            for i in range(len(listaAtividades)):
                print(f'{i}.', listaAtividades[i])
            print('-' * 139)
    else:
        print("Comando inválido, tente novamente!")