import heapq
import sys


N = int(sys.stdin.readline())

maze = []

for _ in range(N):
    m_row = list(map(int, sys.stdin.readline().strip()))
    maze.append(m_row)


def miro(graph, start, end, N):
    visited = set()
    min_cost = [[float("inf") for _ in range(N)] for _ in range(N)]
    pq = []
    heapq.heappush(pq, (0, start))  # (0, (0,0))

    while pq:
        acc_cost, (r, c) = heapq.heappop(pq)
        if (r, c) in visited:
            continue
        visited.add((r, c))

        if acc_cost > min_cost[r][c]:
            continue

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_r = r + dr
            next_c = c + dc
            if 0 <= next_r < N and 0 <= next_c < N:
                is_break = 1 if graph[next_r][next_c] == 0 else 0
                if min_cost[next_r][next_c] > acc_cost + is_break:
                    min_cost[next_r][next_c] = acc_cost + is_break
                    heapq.heappush(pq, (acc_cost + is_break, (next_r, next_c)))

    e_r, e_c = end
    return min_cost[e_r][e_c]


re = miro(maze, (0, 0), (N - 1, N - 1), N)
print(re)
