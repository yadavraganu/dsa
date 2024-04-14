def binary_search(array, item):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == item:
            return mid
        if array[mid] > item:
            end = mid - 1
        elif array[mid] < item:
            start = mid + 1
    return -1


if __name__ == '__main__':
    print(binary_search([1, 2, 4, 5, 6, 9], 9))
    print(binary_search([1, 2, 4, 5, 6, 9], 4))
    print(binary_search([1, 2, 4, 5, 6, 9], 78))
