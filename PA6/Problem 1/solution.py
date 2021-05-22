# Param Somane (pss5256)

def BFS(s, t, prev):
    visited = [0] * n
    Q = [s]
    visited[s] = 1
    while len(Q) != 0:
        u = Q.pop()
        for vertex, capacity in enumerate(Edges[u]):
            if visited[vertex] == False and capacity > 0:
                Q.append(vertex)
                visited[vertex] = True
                prev[vertex] = u
    if visited[t]:
        return True
    return False


n, m = map(int, input().split())
Edges = [[0] * n for v in range(n)]
for i in range(0, m):
    a, b, cap = map(int, input().split())
    a = a - 1
    b = b - 1
    if Edges[a][b] == 0:
        Edges[a][b] = cap
    else:
        Edges[a][b] += cap
prev = [-1] * n
flow = 0
while BFS(0, n - 1, prev):
    path = []
    t = n - 1
    while t != 0:
        path.insert(0, (prev[t], t))
        t = prev[t]
    x_p = min(Edges[e[0]][e[1]] for e in path)
    flow += x_p
    t = n - 1
    while t != 0:
        v = prev[t]
        Edges[v][t] -= x_p
        Edges[t][v] += x_p
        t = prev[t]
print(flow)
