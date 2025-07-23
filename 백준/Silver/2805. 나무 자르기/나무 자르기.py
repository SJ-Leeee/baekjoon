import sys

def sum_woods(woods, cut):
    result = 0
    for wood in woods:
        if wood > cut:
            result += wood - cut
    return result


N, need = map(int, sys.stdin.readline().split())
wood_list = list(map(int, sys.stdin.readline().split()))

wood_list.sort()
left = 0
right = wood_list[-1]
while left < right:
    mid = (left + right) // 2
    target = sum_woods(wood_list, mid)

    if need < target:
        left = mid + 1
    else:
        right = mid
if sum_woods(wood_list, left) < need:
    left = left - 1
print(left)
