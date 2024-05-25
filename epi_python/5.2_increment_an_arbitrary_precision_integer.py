"""Write a program which takes as input an array of digits encoding a non negative decimal integer
D and updates the array to represent the integer D + 1. For example, if the input is (7,2,9) then
you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
language that has finite-precision arithmetic."""


def plus_one(array):
    carry = 1  # Starting with carry as we need to add one
    for i in range(len(array) - 1, -1, -1):
        if carry + array[i] == 10:
            array[i] = 0
            carry = 1
        else:
            array[i] = carry + array[i]
            carry = 0
    if carry == 1:
        array[0] = 1
        array.append(0)
    return array


if __name__ == '__main__':
    print(plus_one([9, 0, 9, 9]))
