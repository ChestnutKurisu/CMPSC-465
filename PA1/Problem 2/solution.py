def merge_sorted_arrays(array_a, array_b):
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
    return array_c


def merge_sort(array_c):
    n_c = len(array_c)
    if n_c <= 1:
        return array_c
    return merge_sorted_arrays(merge_sort(array_c[:n_c // 2]), merge_sort(array_c[n_c // 2:]))


n = int(input())
if n == 0:
    exit(0)
array = list(map(int, input().split(' ')))
sorted_array = merge_sort(array)
for i in sorted_array:
    print(i, end=' ')
