matrizA = [1, 2, 1, 2, 3, 3, 1, 5]
matDiferentes = []

for i in range(len(matrizA)): #Percorre a lista do primeiro ao último elemento
    if matrizA[i] not in matDiferentes: #Compara o índice atual com a lista onde está os elementos diferentes
        matDiferentes.append(matrizA[i]) #Caso a lista de elementos diferentes não possua o mesmo elemento, ele é adicionado
print(len(matDiferentes)) #Imprime na tela a quantidade de elementos diferentes