import sys


N = int(sys.stdin.readline())
for _ in range(N):
    data = sys.stdin.readline().strip()
    arr = list(data)

    result = None
    count = 0
    for i in range(len(arr)):
        char = arr.pop()
        if count < 0:
            result = "NO"
            break

        if char == ")":
            count += 1
        else:
            count -= 1

    if result != None:
        print(result)
    elif count == 0:
        print("YES")
    else:
        print("NO")
