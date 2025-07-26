import sys


def assemble_graph(graph, i):
    visited = set()

    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(i)
    return len(visited) - 1


def count_reachable(graph, start):
    visited = set()
    count = 0

    def dfs(vertex):
        nonlocal count
        visited.add(vertex)
        if vertex != start:  # 시작점 제외
            count += 1

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return count


V, E = map(int, sys.stdin.readline().split())


over_graph = {}
under_graph = {}


for i in range(1, V + 1):  # 정점 생성
    over_graph[i] = []
    under_graph[i] = []

for _ in range(E):
    big, small = map(int, sys.stdin.readline().split())
    over_graph[small].append(big)
    under_graph[big].append(small)  # 간선 생성


count = 0
limit = (V // 2) + 1

for i in range(1, V + 1):
    heavy_count = assemble_graph(over_graph, i)
    light_count = assemble_graph(under_graph, i)

    if heavy_count >= limit or light_count >= limit:
        count += 1

print(count)
