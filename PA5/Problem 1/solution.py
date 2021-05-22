# Param Somane (pss5256)

def binary_search(k, a, b):
    while a <= b:
        m = (a + b) // 2
        if t[m-1] <= s[k-1] < t[m]:
            return m
        elif t[m-1] > s[k-1]:
            b = m
        elif s[k-1] >= t[m]:
            a = m + 1
    return 0


n = int(input())
s = [0] * n
t = [0] * n
v = [0] * n
for i in range(0, n):
    s[i], t[i], v[i] = map(int, input().split())
zipped_lists = zip(t, s, v)
sorted_triples = sorted(zipped_lists)
tuples = zip(*sorted_triples)
t, s, v = [list(tuple) for tuple in tuples]
F = [0] * (n + 1)
pre = [0] * (n + 1)
F[0] = 0
for k in range(1, n + 1):
    pre[k] = binary_search(k, 1, k-1)
    F[k] = max(F[k - 1], F[pre[k]] + v[k-1])
print(F[n])
