def SelectionSort(Lst):
    j=0
    while j<len(Lst):
        min=j
        for i in range(min+1,len(Lst)):
            if Lst[min]>Lst[i]:
                min=i
        Lst[j],Lst[min]=Lst[min],Lst[j]
        j+=1
    return Lst


print(SelectionSort([2,6,7,9,1,300,0]))
