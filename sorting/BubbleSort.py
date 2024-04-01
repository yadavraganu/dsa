def BubbleSort(Lst):
    for i in range(len(Lst)):
        for j in range(i,len(Lst)):
            if Lst[i]>Lst[j]:
                Lst[i],Lst[j]=Lst[j],Lst[i]
    return Lst

print(BubbleSort([2,6,7,9,1,300,0]))
