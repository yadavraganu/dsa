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


def lower_bound_binary_search(array, item):
    """
    lower_bound_binary_search is used to get the index in a sorted array on which data
    would be equal or greater than the item we are searching
    :param array:
    :param item:
    :return:
    """
    start = 0
    end = len(array) - 1
    ans = len(array)
    while start <= end:
        mid = (start + end) // 2
        if array[mid] >= item:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1
    return ans


def upper_bound_binary_search(array, item):
    """
    upper_bound_binary_search is used to get the index in a sorted array on which data
    would be greater than the item we are searching
    :param array:
    :param item:
    :return:
    """
    start = 0
    end = len(array) - 1
    ans = len(array)
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > item:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1
    return ans


if __name__ == '__main__':
    print(binary_search([1, 2, 4, 5, 6, 9], 9))
    print(binary_search([1, 2, 4, 5, 6, 9], 4))
    print(binary_search([1, 2, 4, 5, 6, 9], 78))
    print(lower_bound_binary_search([1, 2, 2, 2, 4, 5, 6, 9], 2))
    print(upper_bound_binary_search([1, 2, 2, 2, 4, 5, 6, 9], 0))
