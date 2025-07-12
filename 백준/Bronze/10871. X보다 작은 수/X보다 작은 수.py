
N, limit_num = map(int, input().split())
numbers = list(map(int, input().split()))

result = []
for number in numbers:
    if number < limit_num:
        result.append(number)

st = " ".join(map(str, result))
print(st)


