import string


def string_to_int(input: str):
    minus_flag = True if input[0] == '-' else False
    if minus_flag:
        input = input[1:]
    res = 0
    for i in range(len(input)):
        idx = string.digits.index(input[i])
        res = res + (idx * (pow(10, len(input) - 1 - i)))
    if minus_flag:
        res = res * -1
    return res


def int_string(input: int):
    minus_flag = True if input < 0 else False
    input = abs(input)
    res = []
    while input != 0:
        rem = input % 10
        string_rem = chr(ord('0') + rem)
        input = input // 10
        res.append(string_rem)
    res = ''.join(res)[::-1]
    if minus_flag:
        res = '-' + res
    return res


if __name__ == '__main__':
    res1 = int_string(230)
    res2 = string_to_int('230')
    print(f'type of result {type(res1)}', res1)
    print(f'type of result {type(res2)}', res2)
