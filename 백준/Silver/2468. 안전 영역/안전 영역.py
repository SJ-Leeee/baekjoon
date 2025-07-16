import sys
import copy

sys.setrecursionlimit(100000)


def safe_area(arr, N, limit):
    count = 0
    for x in range(N):  # 잠긴지역 만들기
        for y in range(N):
            if arr[x][y] > limit:
                arr[x][y] = True
            else:
                arr[x][y] = False
    # is_all_true = all(all(row) for row in arr)
    # is_all_false = not any(any(row) for row in arr)
    # if is_all_true or is_all_false:
    #     return 1

    for x in range(N):
        for y in range(N):
            if arr[x][y] == True:
                safe_area_helper(arr, x, y, N)
                count += 1

    # print("------------------------------")
    # for i in range(N):
    #     print(arr[i])
    # print(count)
    return count


def safe_area_helper(arr, x, y, N):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # 일단 False로 둬야한다.
    arr[x][y] = False

    for dr, dc in direction:
        next_x = x + dr
        next_y = y + dc
        if 0 <= next_x < N and 0 <= next_y < N:
            if arr[next_x][next_y] == True:
                safe_area_helper(arr, next_x, next_y, N)
    return


N = int(input())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_val = max(map(max, data))
max_conut = 0
for i in range(max_val):
    squre = copy.deepcopy(data)
    count = safe_area(squre, N, i)
    max_conut = max(count, max_conut)

# max_val = 0인경우
print(max_conut)