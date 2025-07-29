from collections import deque
import sys

def topological_sort(graph, indegree):
    queue = deque([i for i in range(1, len(indegree)) if indegree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    print(*result)

V, E = map(int, sys.stdin.readline().split())
indegree = [0] * (V + 1)
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    indegree[v] += 1

topological_sort(graph, indegree)