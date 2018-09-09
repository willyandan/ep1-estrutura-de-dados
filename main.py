import random 
from mergesort import mergeSort
from quicksort import quickSort
from selectionsort import selectionSort
def main():
    print("EP 1 - Estrutura de dados")
    vet = list(range(21))
    random.shuffle(vet)
    print(selectionSort(vet))
if __name__ == '__main__':
    main()