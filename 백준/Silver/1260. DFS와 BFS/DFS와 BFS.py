
from collections import deque
import sys


def dfs_iterative(graph, start):
    """반복적 DFS - 스택 오버플로우 방지"""
    visited = [False] * (V + 1)
    result = []
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(node)
            # 역순으로 추가해야 올바른 순서 보장
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)

    print(*result)


def bfs(graph, root):
    visited = [False] * (V + 1)
    result = []
    dq = deque()
    dq.append(root)

    while dq:
        vertex = dq.popleft()

        if visited[vertex]:
            continue
        visited[vertex] = True
        result.append(vertex)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dq.append(neighbor)

    print(*result)


graph = {}
V, E, S = map(int, sys.stdin.readline().split())

for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


for i in range(1, V + 1):
    graph[i].sort()

dfs_iterative(graph, S)
bfs(graph, S)
