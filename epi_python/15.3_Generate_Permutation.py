from itertools import permutations


def permute_1(iterable):
    result = []

    def _perm(start, end=[]):
        if len(start) == 0:
            result.append(end)
        else:
            for i in range(len(start)):
                _perm(start[:i] + start[i + 1 :], end + start[i : i + 1])
        return result

    _perm(iterable)
    return result


def permute_2(iterable):
    result = []

    def _perm(index):
        if len(iterable) == index:
            result.append(iterable[:])
            return
        for i in range(index, len(iterable)):
            iterable[index], iterable[i] = iterable[i], iterable[index]
            _perm(index + 1)
            iterable[index], iterable[i] = iterable[i], iterable[index]

    _perm(0)
    return result


if __name__ == "__main__":
    print(permute_1([1, 2, 3]))
    print(list(permutations([1, 2, 3])))
    print(permute_2([1, 2]))
