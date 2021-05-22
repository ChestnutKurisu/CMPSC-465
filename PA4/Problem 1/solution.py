# Param Somane (pss5256)
n, m, s = map(int, input().split())
s = s - 1
l = {}
Edges = [[] for v in range(n)]
for i in range(0, m):
    a, b, c = map(int, input().split())
    a = a - 1
    b = b - 1
    l[(a, b)] = c
    Edges[b].append(a)
dist = [[0 for x in range(n)] for y in range(n+1)]
for v in range(n):
    if v != s: dist[0][v] = 2147483647
for k in range(1, n+1):
    for v in range(n):
        dist[k][v] = dist[k - 1][v]
        for u in Edges[v]:
            if dist[k][v] > dist[k - 1][u] + l[(u,v)]:
                dist[k][v] = dist[k - 1][u] + l[(u,v)]
flag = False
for v in range(n):
    if not dist[n-1][v]==dist[n][v]:
        flag = True
        break
print(flag)