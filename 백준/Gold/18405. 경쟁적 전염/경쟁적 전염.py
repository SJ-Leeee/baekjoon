from collections import deque
import heapq
import sys


N, V = map(int, sys.stdin.readline().split())
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

virus_map = []

for _ in range(N):
    virus = list(map(int, sys.stdin.readline().split()))
    virus_map.append(virus)

S, X, Y = map(int, sys.stdin.readline().split())


def virus():
    if S == 0:
        print(virus_map[X - 1][Y - 1])
        return

    clean_zone = 0
    start_temp = []
    for r in range(N):
        for c in range(N):
            if virus_map[r][c]:

                start_temp.append((virus_map[r][c], r, c))
            else:
                clean_zone += 1
    start_temp.sort()
    dq = deque()
    dq.extend(start_temp)

    temp = []

    for _ in range(S):
        if clean_zone == 0:
            break
        while dq:
            virus, r, c = dq.popleft()

            for dr, dc in direct:
                n_r = r + dr
                n_c = c + dc
                if 0 <= n_r < N and 0 <= n_c < N:
                    if not virus_map[n_r][n_c]:
                        virus_map[n_r][n_c] = virus
                        temp.append((virus, n_r, n_c))

                        clean_zone -= 1
        dq.extend(temp)
        temp = []

    print(virus_map[X - 1][Y - 1])


virus()