w, h = map(int, input().split())
N = int(input())
x_arr = [w]
y_arr = [h]

for _ in range(N):
    direct, cut = map(int, input().split())
    if direct:
        x_arr.append(cut)
    else:
        y_arr.append(cut)

x_arr = sorted(x_arr)
y_arr = sorted(y_arr)

result = []

for i in range(len(x_arr)):
    if i == 0:
        x = x_arr[i]
    else:
        x = x_arr[i] - x_arr[i - 1]

    for j in range(len(y_arr)):
        if j == 0:
            y = y_arr[j]
        else:
            y = y_arr[j] - y_arr[j - 1]
        result.append(x * y)

print(max(result))