import sys


graph = {}
V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs_recursion():
    result = []
    visited = [False] * (V + 1)

    def dfs(v):
        visited[v] = True
        result.append(v)
        for n_v in graph[v]:
            if not visited[n_v]:
                dfs(n_v)

    dfs(1)
    print(len(result) - 1)


dfs_recursion()
