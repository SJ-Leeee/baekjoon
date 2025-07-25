from collections import deque
import sys


def bfs(s_v):
    if s_v == None:
        s_v = list(injeop_list.keys())[0]

    dq = deque()
    result = []
    visited = set()
    dq.append(s_v)
    visited.add(s_v)

    while len(dq) > 0:
        removed = dq.popleft()

        result.append(removed)
        for item in injeop_list[removed]:
            if item not in visited:
                visited.add(item)
                dq.append(item)

    return result


R, C = map(int, sys.stdin.readline().split())
# visited = [[False for _ in range(C)] for _ in range(R)]
ice_map = []
injeop_list = {}

for _ in range(R):
    data = list(map(int, sys.stdin.readline().split()))
    ice_map.append(data)

for i in range(R):
    for j in range(C):
        if ice_map[i][j] != 0:
            injeop_list[(i, j)] = []
            for r, c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if ice_map[i + r][j + c] != 0:
                    injeop_list[(i, j)].append((i + r, j + c))

count = 0
while len(injeop_list) > 0:
    key_list = list(injeop_list.keys())
    all_keys = bfs(None)
    if len(key_list) != len(all_keys): # 비교
        break

    for r, c in key_list:  # 감소
        discount = 4 - len(injeop_list[(r, c)])
        ice_map[r][c] -= discount

    for r, c in key_list:  # 삭제
        if ice_map[r][c] <= 0:
            while len(injeop_list[(r, c)]) > 0:
                e_r, e_c = injeop_list[(r, c)].pop()
                injeop_list[(e_r, e_c)] = [
                    item for item in injeop_list[(e_r, e_c)] if item != (r, c)
                ]

            del injeop_list[(r, c)]
    count += 1

if len(injeop_list) == 0:
    print(0)
else:
    print(count)