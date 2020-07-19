matrizA = [9, 3, 9, 3, 9, 7, 9, 7, 2]
matIguais = []
matUnic = []

for i in range(len(matrizA)): #Percorre a matriz inteira começando da primeira posição até a última.
    for j in range(len(matrizA)-1, i, -1): #Percorre a matriz inteira da última posição até a primeira.
        if matrizA[i] == matrizA[j]: #Verifica se a matriz atual (posição i) é igual a alguma das próximas posições.
            matIguais.append(matrizA[i]) #Caso verdadeira a linha de cima, esse elemento é adicionado a lista de iguais.

for i in range(len(matrizA)): #Percorre a matriz inteira começando da primeira posição até a última.
    if matrizA[i] not in matIguais: #Verifica se o elemento da matriz na posição atual está inserida na matriz de elementos iguais.
        matUnic.append(matrizA[i]) #Caso ainda não esteja, significa que este elemento é único e é adicionado a matriz dos unicos.
print(matUnic) #Imprime na tela o elemento que não está emparelhado com nenhum outro elemento.