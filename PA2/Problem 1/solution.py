def merge_and_count(array_a, array_b, pairs):
    array_c = []
    len_c = len(array_a) + len(array_b)
    array_a.append(2147483648)
    array_b.append(2147483648)
    pointer_a = 0
    pointer_b = 0
    for i in range(len_c):
        if array_a[pointer_a] <= array_b[pointer_b]:
            array_c.append(array_a[pointer_a])
            pointer_a += 1
        else:
            array_c.append(array_b[pointer_b])
            pointer_b += 1
            if array_a[pointer_a] != 2147483648:
                pairs += (len(array_a) - 1 - pointer_a)
    return [array_c, pairs]


def count_pairs(array_c, pairs):
    n_c = len(array_c)
    if n_c <= 1:
        return [array_c, 0]
    tup_a = count_pairs(array_c[:n_c // 2], pairs)
    tup_b = count_pairs(array_c[n_c // 2:], pairs)
    return merge_and_count(tup_a[0], tup_b[0], tup_a[1] + tup_b[1])


n = int(input())
if n == 0:
    exit(0)
A = list(map(int, input().split(' ')))
print(count_pairs(A, 0)[1])
