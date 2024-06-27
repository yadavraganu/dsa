import string


def string_to_decimal(input: str, base: int):
    res = 0
    for i in range(len(input)):
        idx = string.hexdigits.index(input[i].lower())
        res = res + pow(base, len(input) - 1 - i) * idx
    return res


def decimal_string(input: int, base: int):
    res = []
    while input != 0:
        rem = input % base
        rem_string = string.hexdigits[rem].upper()
        input = input // base
        res.append(rem_string)
    res = ''.join(res)[::-1]
    return res


if __name__ == '__main__':
    print(string_to_decimal('30A8', 16))
    print(decimal_string(124563143144, 16))
