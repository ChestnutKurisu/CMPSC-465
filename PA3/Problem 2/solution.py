# Param Somane (pss5256)

from queue import PriorityQueue

# Note that PriorityQueue is implemented using heapq

n, m, s = map(int, input().split())
Edges = {}
for i in range(0, m):
    a, b, c = map(int, input().split())
    Edges[(a, b)] = c
dist = [2147483647] * n
PQ = PriorityQueue()
for i in range(1, n + 1):
    PQ.put((2147483647, i))
dist[s - 1] = 0
PQ.put((0, s))
visited = [0] * n
while not PQ.empty():
    u = PQ.get()
    if visited[u[1] - 1] == 1:
        continue
    for e in Edges:
        if not e[0] == u[1]:
            continue
        if dist[e[1] - 1] > dist[e[0] - 1] + Edges[e]:
            dist[e[1] - 1] = dist[e[0] - 1] + Edges[e]
            PQ.put((dist[e[1] - 1], e[1]))
        visited[u[1] - 1] = 1

for i in range(0, n):
    if dist[i] == 2147483647:
        print(-1)
    else:
        print(dist[i])
