import random, timeit
from mergesort import mergeSort
from quicksort import quickSort
from selectionsort import selectionSort
def main():
    vetor = []
    total = 0
    i=0
    print("="*66)
    print("||"+"Teste de velocidade".center(62)+"||")
    print("="*66)  
    print("||"+
        "Selection\t"+"||"+
        "Quick\t\t"+"||"+
        "Merge\t\t"+"||"+
        "Native\t"+"||")
    print("="*66)  
    while total <= 30:
        geraVetor(vetor,i)
        i+=2000
        selection_time = test(selectionSort,vet=vetor.copy())
        quick_time = test(quickSort,vet=vetor.copy())
        merge_time = test(mergeSort,vet=vetor.copy())
        native_time = test(None,vet=vetor.copy())
        print(
            "||"+
            "%.2f\t\t"%selection_time+"||"+
            "%.2f\t\t"%quick_time+"||"+
            "%.2f\t\t"%merge_time+"||"+
            "%.2f\t\t"%native_time+"||"
        )
        total = selection_time + quick_time +  merge_time + native_time
    print("="*66) 
def geraVetor(vet, n):
    vetor = list(range(n, n+2000))
    random.shuffle(vetor)
    vet.extend(vetor)
def test(sort_func=None, vet=[]):
    if not sort_func:
        x = timeit.Timer(lambda: vet.sort()).timeit(number=1)
    else:
        x = timeit.Timer(lambda: sort_func(vet)).timeit(number=1)
    return float("{0:.4f}".format(x))
if __name__ == '__main__':
    main()