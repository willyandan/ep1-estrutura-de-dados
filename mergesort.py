def mergeSort(vet):
    if(len(vet) < 2): return vet
    meio = len(vet)//2 
    return merge(rlist=mergeSort(vet[meio:]), llist=mergeSort(vet[:meio]))
    
def merge(rlist =[], llist = []):
    final = []
    while rlist and llist:
        if llist[0] < rlist[0]:
            final.append(llist.pop(0))
        else:
            final.append(rlist.pop(0))
    if(llist): return final + llist
    if(rlist): return final + rlist
    return final
