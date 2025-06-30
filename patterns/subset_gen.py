lst = [1,2,3]
def subset_gen(index,lst,res):
    if index == len(lst)-1:
        return
    res = res.append(lst[index])
    subset_gen(index,lst,res)

