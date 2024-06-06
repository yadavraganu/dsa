"""
Write a program which takes an array of n integers, where A[i] denotes the maximum you can
advance from index i, and returns whether it is possible to advance to the last index starting from
the beginning of the array.
"""


def advancing_array(arr):
    max_travel = 0
    i = 0
    while i <= max_travel and i < len(arr):
        max_travel = max(arr[i] + i, max_travel)
        if max_travel > len(arr) - 1:
            return True
        i += 1
    return False


if __name__ == '__main__':
    arr = [3, 3, 1, 0, 2, 0, 1]
    print(advancing_array(arr))
    arr = [3, 2, 0, 0, 2, 0, 1]
    print(advancing_array(arr))
