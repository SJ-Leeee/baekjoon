
from collections import deque
import sys

dark_map = []
start_water = []
start_goseum = None
end_goseum = None  # 초기세팅

ROW, COL = map(int, sys.stdin.readline().split())

for _ in range(ROW):
    line = list(sys.stdin.readline().strip())
    dark_map.append(line)

for i in range(ROW):
    for j in range(COL):
        if dark_map[i][j] == "*":
            start_water.append((i, j))
        elif dark_map[i][j] == "S":
            start_goseum = (i, j)
        elif dark_map[i][j] == "D":
            end_goseum = (i, j)


def dijkstra(graph, start_list):  # 물의 이동방향을 체크
    dq = deque()
    min_cost_dict = [[float("inf") for _ in range(COL)] for _ in range(ROW)]

    visited = set()

    for r, c in start_list:
        dq.append((0, r, c))
        min_cost_dict[r][c] = 0

    while dq:
        cost, c_r, c_c = dq.popleft()
        if (c_r, c_c) in visited:
            continue
        visited.add((c_r, c_c))
        if cost > min_cost_dict[c_r][c_c]:
            continue

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_r = c_r + dr
            next_c = c_c + dc
            if 0 <= next_r < ROW and 0 <= next_c < COL:  # 일단 범위안에 있어야 하고
                if graph[next_r][next_c] == "D" or graph[next_r][next_c] == "X":
                    continue
                if min_cost_dict[next_r][next_c] > cost + 1:
                    dq.append((cost + 1, next_r, next_c))
                    min_cost_dict[next_r][next_c] = cost + 1
    return min_cost_dict


def dijkstra2(graph, water_graph, start, end):  # 물의 이동방향을 기준으로 최소값
    dq = deque()
    min_cost_dict = [[float("inf") for _ in range(COL)] for _ in range(ROW)]

    visited = [[False for _ in range(COL)] for _ in range(ROW)]

    s_r, s_c = start
    dq.append((0, s_r, s_c))
    min_cost_dict[s_r][s_c] = 0

    while dq:
        cost, c_r, c_c = dq.popleft()
        if (c_r, c_c) == end:
            break
        if visited[c_r][c_c]:
            continue
        visited[c_r][c_c] = True

        if cost > min_cost_dict[c_r][c_c]:  # 최소값을가는게 제일좋은건아닌데
            continue

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_r = c_r + dr
            next_c = c_c + dc
            if 0 <= next_r < ROW and 0 <= next_c < COL:  # 일단 범위안에 있어야 하고
                if graph[next_r][next_c] == "X":
                    continue
                if (
                    water_graph[next_r][next_c] > cost + 1
                    and min_cost_dict[next_r][next_c] > cost + 1
                ):
                    dq.append((cost + 1, next_r, next_c))
                    min_cost_dict[next_r][next_c] = cost + 1
    e_r, e_c = end

    if min_cost_dict[e_r][e_c] == float("inf"):
        return "KAKTUS"
    else:
        return min_cost_dict[e_r][e_c]


water_graph = dijkstra(dark_map, start_water)
answer = dijkstra2(dark_map, water_graph, start_goseum, end_goseum)
print(answer)
