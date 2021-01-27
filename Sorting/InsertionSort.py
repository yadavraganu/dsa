def insertion_sort_with_swapping(Lst):
    for i in range(1,len(Lst)):
        j=i-1
        while(j>=0 and Lst[j]>Lst[j+1]):
                Lst[j],Lst[j+1]=Lst[j+1],Lst[j]
                j=j-1
    return Lst
def insertion_sort_without_swapping(Lst):
    for i in range(1,len(Lst)):
        j=i-1
        curr=Lst[i]
        while(j>=0 and Lst[j]>curr):
            Lst[j+1]=Lst[j]
            j=j-1
        Lst[j+1]=curr
    return Lst
print(insertion_sort_with_swapping([2,6,7,9,1,300,0,54545,4,0,5,2,2,4,10,50,40,30]))
print(insertion_sort_without_swapping([2,6,7,9,1,300,0,54545,4,0,5,2,2,4,10,50,40,30]))
