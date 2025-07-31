from collections import deque
import sys


N = int(sys.stdin.readline())

apart_map = []
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = set()
for _ in range(N):
    line = list(map(int, sys.stdin.readline().strip()))
    apart_map.append(line)


def bfs(r, c):

    dq = deque()
    dq.append((r, c))
    visited.add((r, c))
    temp_count = 0

    while dq:
        cur_r, cur_c = dq.popleft()

        temp_count += 1

        for dr, dc in direct:
            nr = cur_r + dr
            nc = cur_c + dc
            if (
                0 <= nr < N
                and 0 <= nc < N
                and apart_map[nr][nc] == 1
                and (nr, nc) not in visited
            ):  # 1이라면
                visited.add((nr, nc))
                dq.append((nr, nc))
    return temp_count


result = []

for r in range(N):
    for c in range(N):
        if (r, c) not in visited and apart_map[r][c] == 1:
            cnt = bfs(r, c)
            result.append(cnt)

result.sort()
print(len(result))
for i in result:
    print(i)
