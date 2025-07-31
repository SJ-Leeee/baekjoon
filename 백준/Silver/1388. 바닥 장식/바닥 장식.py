import sys

R, C = map(int, sys.stdin.readline().split())

wood_map = []
for _ in range(R):
    wood = list(sys.stdin.readline().strip())
    wood_map.append(wood)


visited = set()


def dfs(r, c, prev):
    global visited
    visited.add((123, 123))
    if prev != wood_map[r][c]:
        return

    visited.add((r, c))

    if wood_map[r][c] == "-":
        if c + 1 < C:
            dfs(r, c + 1, wood_map[r][c])

    else:
        if r + 1 < R:
            dfs(r + 1, c, wood_map[r][c])


count = 0
for r in range(R):
    for c in range(C):
        if (r, c) not in visited:
            count += 1
            dfs(r, c, wood_map[r][c])

print(count)
