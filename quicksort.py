def quickSort(vet):
    if len(vet) <= 1: return vet
    pivo = vet[0]
    maior = [val for val in vet if val > pivo]
    menor = [val for val in vet if val < pivo]
    igual = [val for val in vet if val == pivo]
    return quickSort(menor) + igual + quickSort(maior)
    