"""Write a program that takes an array A and an index i into A, and rearranges the elements such
that all elements less than A[i] (the "pivot") appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot."""


def dutch_national_flag_problem(array, pivot):
    smaller, larger = 0, len(array)
    pivot_element = array[pivot]
    equal = 0
    while equal < larger:
        if array[equal] < pivot_element:
            array[equal], array[smaller] = array[smaller], array[equal]
            smaller += 1
            equal += 1
        elif array[equal] == pivot_element:
            equal += 1
        else:
            larger -= 1
            array[equal], array[larger] = array[larger], array[equal]

    return array


if __name__ == '__main__':
    arr = [3, 5, 677, 9, 2, 34345, 2345, 2]
    print(dutch_national_flag_problem(arr, 3))
