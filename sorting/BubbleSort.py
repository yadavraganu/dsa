def BubbleSort(Lst):
    """
    swap variable added to break the loop
    if list is sorted before reaching final
    iteration.It is just for optimization

    """
    for i in range(len(Lst)):
        swap = False
        for j in range(i, len(Lst)):
            if Lst[i] > Lst[j]:
                Lst[i], Lst[j] = Lst[j], Lst[i]
                swap = True
        if not swap:
            break
    return Lst


if __name__ == '__main__':
    print(BubbleSort([2, -6, -7, 9, 1, 300, 0]))
