def linear_search(array, item):
    for i in range(0, len(array)):
        if array[i] == item:
            return i
    return -1


if __name__ == '__main__':
    print(linear_search([1, 2, 345, 4, 231, 3], 4))
    print(linear_search([1, 2, 345, 4, 231, 3], 4231))
