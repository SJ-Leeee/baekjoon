from collections import deque
import sys

def solve():
    # 입력 처리
    R, C = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(R)]
    
    # 시작점들 찾기
    water_queue = deque()
    hedgehog_pos = None
    dest_pos = None
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '*':
                water_queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 'S':
                hedgehog_pos = (r, c)
            elif grid[r][c] == 'D':
                dest_pos = (r, c)
    
    # 물의 확산 시간 계산 (BFS)
    water_time = [[float('inf')] * C for _ in range(R)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 물의 확산 BFS
    while water_queue:
        r, c, time = water_queue.popleft()
        if water_time[r][c] <= time:
            continue
        water_time[r][c] = time
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < R and 0 <= nc < C and 
                grid[nr][nc] != 'X' and grid[nr][nc] != 'D' and
                water_time[nr][nc] > time + 1):
                water_queue.append((nr, nc, time + 1))
    
    # 고슴도치 이동 BFS
    hedgehog_queue = deque([(*hedgehog_pos, 0)])  # (row, col, time)
    visited = [[False] * C for _ in range(R)]
    visited[hedgehog_pos[0]][hedgehog_pos[1]] = True
    
    while hedgehog_queue:
        r, c, time = hedgehog_queue.popleft()
        
        # 목적지 도달
        if (r, c) == dest_pos:
            return time
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < R and 0 <= nc < C and 
                not visited[nr][nc] and grid[nr][nc] != 'X' and
                water_time[nr][nc] > time + 1):  # 물보다 먼저 도착해야 함
                visited[nr][nc] = True
                hedgehog_queue.append((nr, nc, time + 1))
    
    return "KAKTUS"

print(solve())