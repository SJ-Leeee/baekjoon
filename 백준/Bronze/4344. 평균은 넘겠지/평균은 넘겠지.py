N = int(input())
for _ in range(N):
    data = list(map(int, input().split()))
    n = data[0]
    scores = data[1:]

    pass_count = 0
    average = sum(scores) / n

    for score in scores:
        if score > average:
            pass_count += 1

    pass_ratio = round((pass_count / n) * 100, 3)
    print(f"{pass_ratio:.3f}%")
