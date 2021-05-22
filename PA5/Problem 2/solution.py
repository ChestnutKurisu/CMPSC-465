# Param Somane (pss5256)


def find(x):
    while x.parent != x:
        x = x.parent
    return x


def make_set(x):
    x.height = 1
    x.parent = x


def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return
    if rx.height < ry.height:
        rx.parent = ry
        ry.height += rx.height
    else:
        ry.parent = rx
        rx.height += ry.height


class Node:
    def __init__(self, data, height, parent):
        self.data = data
        self.height = height
        self.parent = parent


n, m = map(int, input().split())
V = []
for v in range(0, n):
    V.append(Node(v, 0, None))
    make_set(V[v])
l = {}
for i in range(0, m):
    a, b, c = map(int, input().split())
    if not (V[a - 1], V[b - 1]) in l or l[(V[a - 1], V[b - 1])] > c:
        l[(V[a - 1], V[b - 1])] = c
l = dict(sorted(l.items(), key=lambda item: item[1]))
s = 0
for e in l.keys():
    ru = find(e[0])
    rv = find(e[1])
    if ru != rv:
        s += l[e]
        union(ru, rv)
print(s)
