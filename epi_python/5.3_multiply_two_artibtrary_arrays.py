"""
Write a program that takes two arrays representing integers, and returns an integer array representing their product
"""


def multiply(num1, num2):
    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            temp_mult = (num1[i] * num2[j]) + result[i + j + 1]
            carry = (temp_mult // 10) + result[i + j]
            res = temp_mult % 10
            result[i + j + 1] = res
            result[i + j] = carry
    return result


if __name__ == '__main__':
    import random

    for i in range(1, 3):
        num1 = random.randrange(1, 99999999)
        num2 = random.randrange(1, 99999999)
        num1_list = list(map(int, list(str(num1))))
        num2_list = list(map(int, list(str(num2))))
        result = int(''.join(map(str, multiply(num1_list, num2_list))))

        if num1 * num2 == result:
            print(f"Num1 : {num1_list}\nNum2 : {num2_list} \nResult : {result}\nStatus : Correct Result")
        else:
            print(f"Num1 : {num1_list}\nNum2 : {num2_list} \nResult : {result}\nStatus : Incorrect Result")
