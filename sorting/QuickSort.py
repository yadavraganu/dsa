def quick_sort(Lst):
    low=0
    high=len(Lst)-1
    quick_recursive(Lst,low,high)
    return Lst

    
def quick_recursive(Lst,low,high):
    if low<high:
        p=get_pointer(Lst,low,high)
        quick_recursive(Lst,low,p-1)
        quick_recursive(Lst,p+1,high)


def get_pointer(Lst,low,high):
    pivot_index,pivot_value=get_pivot(Lst,low,high)
    Lst[pivot_index],Lst[low]=Lst[low],Lst[pivot_index]
    pointer=low
    for i in range(low,high+1):
        if Lst[i]<pivot_value:
            pointer+=1
            Lst[i],Lst[pointer]=Lst[pointer],Lst[i]
    Lst[pointer],Lst[low]=Lst[low],Lst[pointer]
    return pointer


def get_pivot(Lst,low,high):
    mid=(low+high)//2
    if (Lst[low]>Lst[mid]) or (Lst[low]>Lst[high]):
        pivot=low
    elif (Lst[mid]>Lst[low]) or (Lst[mid]>Lst[high]):
        pivot=mid
    else:
        pivot=high
    return pivot,Lst[pivot]


print(quick_sort([2,6,7,9,1,300,0,54545,4,0,5,2,2,4,10,50,40,30]))
