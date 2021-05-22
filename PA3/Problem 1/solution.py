# Param Somane (pss5256)

visited = []
pre = []
post = []
postlist = []
clock = 0
num_cc = 0


def DFS_with_timing(V, E):
    global visited, pre, post, clock
    visited = [0] * V
    pre = [0] * V
    post = [0] * V
    clock = 1
    for i in range(1, V+1):
        if visited[i-1] == 0: explore(E, i)


def explore(E, i):
    global visited, pre, post, postlist, clock
    visited[i-1] = 1
    pre[i-1] = clock
    clock = clock + 1
    for e in E.keys():
        if e[0] != i: continue
        if visited[e[1]-1] == 0: explore(E, e[1])
    post[i-1] = clock
    clock = clock + 1
    postlist.append(i)


def explore_2(E, i):
    global visited, num_cc
    visited[i-1] = num_cc
    for e in E.keys():
        if e[0] != i: continue
        if visited[e[1]-1] == 0: explore_2(E, e[1])


if __name__ == "__main__":
    n, m = map(int, input().split())
    Edges = {}
    ReverseEdges = {}
    for i in range(0, m):
        a, b = map(int, input().split())
        Edges[(a, b)] = 0
        ReverseEdges[(b, a)] = 0
    DFS_with_timing(n, ReverseEdges)
    postlist.reverse()
    specific_order = postlist
    # Running DFS on G = (n, Edges)
    visited = [0] * n
    for i in specific_order:
        if visited[i-1] == 0:
            num_cc = num_cc + 1
            explore_2(Edges, i)
    print(num_cc)
