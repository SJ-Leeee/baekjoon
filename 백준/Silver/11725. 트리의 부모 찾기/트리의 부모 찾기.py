import sys
sys.setrecursionlimit(100000)

graph = {}
V = int(sys.stdin.readline())

for i in range(1, V + 1):
    graph[i] = []

for _ in range(V - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs_recur():
    previous = [False] * (V + 1)
    visited = [False] * (V + 1)

    def dfs(v):
        visited[v] = True

        for n_v in graph[v]:
            if not visited[n_v]:
                previous[n_v] = v
                dfs(n_v)

    dfs(1)
    return previous


a = dfs_recur()
for i in range(2, V + 1):
    print(a[i])
