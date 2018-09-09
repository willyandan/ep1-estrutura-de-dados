import random, mergesort, quicksort
def main():
    print("EP 1 - Estrutura de dados")
    vet = list(range(21))
    random.shuffle(vet)
    print(quicksort.quickSort(vet))
if __name__ == '__main__':
    main()