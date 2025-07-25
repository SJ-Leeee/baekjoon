
def dfs_recursive(start):
    visited = set()
    cnt = 0

    def dfs(vertex):
        nonlocal cnt  # 외부 cnt 수정
        visited.add(vertex)
        for neighbor in adjacency_list[vertex]:  # list{ 1: [2,3]}

            if neighbor not in visited:
                if is_inside[neighbor - 1] == 1:
                    cnt += 1
                else:
                    dfs(neighbor)

    dfs(start)
    return cnt


import sys

adjacency_list = {}

N = int(sys.stdin.readline())

is_inside = list(map(int, sys.stdin.readline().strip()))

for i in range(1, N + 1):
    adjacency_list[i] = []

for _ in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    adjacency_list[v1].append(v2)
    adjacency_list[v2].append(v1)


count = 0
for i in range(1, len(is_inside) + 1):
    if is_inside[i - 1] == 1:
        count += dfs_recursive(i)

print(count)
