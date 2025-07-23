import sys


gun_num, animal_num, L = map(int, sys.stdin.readline().split())

guns = list(map(int, sys.stdin.readline().split()))

animals = []
for _ in range(animal_num):
    x, y = map(int, sys.stdin.readline().split())
    animals.append((x, y))

guns.sort()

cnt = 0
for location in animals:
    x, y = location
    if y > L:
        continue
    min_range = x - (L - y)
    max_range = x + (L - y)
    hi = len(guns)
    lo = 0

    while lo < hi:
        mid = (lo + hi) // 2

        if guns[mid] >= min_range and guns[mid] <= max_range:
            # 포함 된다면
            cnt += 1
            break
        elif guns[mid] < min_range:
            lo = mid + 1
        elif guns[mid] > max_range:
            hi = mid


print(cnt)
