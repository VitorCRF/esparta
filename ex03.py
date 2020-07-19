n = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
m = 4
cont = 0
i = 0
while True: #Loop infinito
    if n[i] == 1: #Verifica se o chocolate está ali ou é somente a embalagem, 1 representa o chocolate e 0 a embalagem.
        n[i] = 0 #Caso seja 1, o chocolate é comido e a na posição resta a embalagem.
        i = i + m #O próximo chocolate será m posições a partir do ultimo.
        cont = cont + 1 #Contador de chocolates comidos recebe + 1.
        if i + m >= len(n): #Verifica se a posição do próximo chocolate excede o tamanho da lista.
            n[i] = 0 #Caso positivo a linha de cima, a sua posição é alterada para 0.
            i = len(n) - i #A próxima posição será o tamanho da lista subtraindo a posição atual.
            cont = cont + 1 #Contador de chocolates comidos recebe + 1.
    else: #Se o n na posição atual for diferente do inteiro 1, significa que o programa encontrou uma embalagem vazia.
        break #Com essa condição o programa é encerrado.
print(cont) #Mostra na tela a quantidade de chocolates comidos.