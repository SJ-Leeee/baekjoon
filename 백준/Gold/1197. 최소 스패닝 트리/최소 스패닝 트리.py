import heapq
import sys

graph = {}
V, E = map(int, sys.stdin.readline().split())

for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2, c = map(int, sys.stdin.readline().split())
    graph[v1].append((c, v2))
    graph[v2].append((c, v1))


def prim_mst():
    visited = set()
    visited.add(1)

    pq = []

    for c, n in graph[1]:
        heapq.heappush(pq, (c, n))

    sum_edge = []
    while pq and len(visited) < V:
        # 여기서 추가
        cost, cur_ver = heapq.heappop(pq)

        if cur_ver in visited:
            continue

        visited.add(cur_ver)
        sum_edge.append(cost)

        for n_cost, n_ver in graph[cur_ver]:
            if n_ver not in visited:
                heapq.heappush(pq, (n_cost, n_ver))

    print(sum(sum_edge))


prim_mst()
