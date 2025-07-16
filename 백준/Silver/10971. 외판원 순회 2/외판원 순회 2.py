import sys


min_cost = float("inf")


def traveling_salesperson_problem(arr, result, visited, depth, d_sum):
    global min_cost
    if depth == len(arr) - 1:
        if arr[result[depth - 1]][0] == 0:
            return  # 돌아갈 수 없으면 무효
        d_sum += arr[result[depth - 1]][0]
        min_cost = min(d_sum, min_cost)
        return

    for i in range(len(arr)):  # 항상 모든원소를 순회
        if not visited[i]:  # 원소가 선택되지 않았더라면
            cur_loca = result[depth - 1]
            if arr[cur_loca][i] == 0:
                continue
            visited[i] = True  # 해당원소 사용
            d_sum += arr[cur_loca][i]  # 더하기
            result[depth] = i
            traveling_salesperson_problem(arr, result, visited, depth + 1, d_sum)
            d_sum -= arr[cur_loca][i]
            visited[i] = False  # 해당원소 사용중지


N = int(input())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [0] * len(data)
visited = [False] * len(data)
visited[0] = True


traveling_salesperson_problem(data, result, visited, 0, 0)
print(min_cost)