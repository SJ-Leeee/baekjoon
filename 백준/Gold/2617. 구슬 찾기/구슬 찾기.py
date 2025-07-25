
import sys


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


for i in range(1, V + 1):
    over_graph[i] = []
    under_graph[i] = []

for _ in range(E):
    big, small = map(int, sys.stdin.readline().split())
    over_graph[small].append(big)
    under_graph[big].append(small)


# over_graph = assemble_graph(over_graph, V)


# under_graph = assemble_graph(under_graph, V)


count = 0
limit = (V // 2) + 1

for i in range(1, V + 1):
    heavy_count = count_reachable(over_graph, i)
    light_count = count_reachable(under_graph, i)

    if heavy_count >= limit or light_count >= limit:
        count += 1

print(count)