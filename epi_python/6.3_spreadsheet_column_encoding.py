def ss_decode_id(col: str):
    res = 0
    for i in range(len(col)):
        idx = ord(col[i].upper()) - 64
        res = res + pow(26, len(col) - 1 - i) * idx
    return res


print(ss_decode_id('CCC'))
