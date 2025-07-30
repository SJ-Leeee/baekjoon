import sys

sys.setrecursionlimit(200000)

graph = {}
N = int(sys.stdin.readline())
is_inside = [0] + list(map(int, sys.stdin.readline().strip()))
for i in range(1, N + 1):
    graph[i] = []

for _ in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def morning_walk(graph, is_inside):
    visited = set()
    acc_cnt = 0
    temp_cnt = 0

    def dfs_out(start):
        nonlocal temp_cnt
        visited.add(start)

        for n_v in graph[start]:
            if is_inside[n_v]:  # 실내라면 숫자만 추가하고
                temp_cnt += 1
            else:  # 실외면 더 들어가자
                if n_v not in visited:
                    dfs_out(n_v)

    def dfs_in(start):
        nonlocal temp_cnt
        visited.add(start)

        for n_v in graph[start]:
            if is_inside[n_v] and n_v not in visited:  # 방문하지 않았고, 실내면 추가
                temp_cnt += 1
                dfs_in(n_v)
            # else: # 방문한적이 있거나, 실외면
            # temp_cnt = 0

    for i in range(1, len(is_inside)):
        if not is_inside[i] and i not in visited:  # 0이고 방문하지 않았던 실외
            dfs_out(i)
            acc_cnt += temp_cnt * (temp_cnt - 1)
            temp_cnt = 0
        if is_inside[i] and i not in visited:

            dfs_in(i)
            temp = temp_cnt if temp_cnt > 0 else 0
            acc_cnt += temp * 2
            temp_cnt = 0

    print(acc_cnt)
    # dfs


morning_walk(graph, is_inside)
