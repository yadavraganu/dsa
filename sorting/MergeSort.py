def divide(Lst):
    low = 0
    high = len(Lst) - 1
    mid = (low + high + 1) // 2
    right_Lst = Lst[0:mid]
    left_Lst = Lst[mid:]
    return right_Lst, left_Lst


def merge(Lst, right_Lst, left_Lst):
    i = 0
    j = 0
    k = 0
    # Compare Divided Arrays & Create New
    while i < len(right_Lst) and j < len(left_Lst):
        if right_Lst[i] < left_Lst[j]:
            Lst[k] = right_Lst[i]
            i += 1
        else:
            Lst[k] = left_Lst[j]
            j += 1
        k += 1
    # Enter Remaining element if right array was having more elements than left
    while i < len(right_Lst):
        Lst[k] = right_Lst[i]
        k += 1
        i += 1
    # Enter Remaining element if left array was having more elemnts than right
    while j < len(left_Lst):
        Lst[k] = left_Lst[j]
        k += 1
        j += 1


def mergeSort(Lst):
    if len(Lst) == 1:
        return
    right_Lst, left_Lst = divide(Lst)
    mergeSort(right_Lst)
    mergeSort(left_Lst)
    merge(Lst, right_Lst, left_Lst)


if __name__ == '__main__':
    array = [21, 6, 7, 9, 1, 300, 0, -1]
    mergeSort(array)
    print(array)
