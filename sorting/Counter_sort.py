def counting_sort(lst):
    l = len(lst)
    l_max = max(lst)
    c_lst = [0] * (l_max + 1)
    for i in lst:
        c_lst[i] += 1
    for j in range(1, l_max + 1):
        c_lst[j] += c_lst[j - 1]
    o_lst = [0] * l
    for k in range(l - 1, -1, -1):
        o_lst[c_lst[lst[k]] - 1] = lst[k]
        c_lst[lst[k]] -= 1
    return o_lst


if __name__ == "__main__":
    print(counting_sort([2, 6, 7, 9, 1, 300, 0, 5, 4, 0, 5, 2, 1, 50, 40, 30]))
    print(counting_sort([2, 60, 1, 1, 2, 3, 14, 134, 3, 40, 30]))
