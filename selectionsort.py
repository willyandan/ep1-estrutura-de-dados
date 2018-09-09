def selectionSort(vet):
    for i in range(len(vet)):
        mini = i
        for j in range(i, len(vet)):
            if vet[j] < vet[mini]:
                mini = j
        if(mini != i):
            aux = vet[i]
            vet[i] = vet[mini]
            vet[mini] = aux
    return vet