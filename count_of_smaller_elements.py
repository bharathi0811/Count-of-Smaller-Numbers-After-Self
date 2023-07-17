l = list(map(int,input("nums = ").split()))
def count_of_small_num(l):
    n = len(l)
    lst = []
    for i in range(0, n):
        count = 0
        for j in range(i + 1, n):
            if l[i] > l[j]:
                count += 1
        lst.append(count)
    return lst
print(count_of_small_num(l))
