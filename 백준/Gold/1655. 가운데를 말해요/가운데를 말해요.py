import heapq
import sys


leftheap = []
rightheap = []


N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    if len(leftheap) == 0 or -leftheap[0] > num:
        heapq.heappush(leftheap, -num)
    else:
        heapq.heappush(rightheap, num)

    if len(leftheap) > len(rightheap) + 1:
        move_node = -heapq.heappop(leftheap)
        heapq.heappush(rightheap, move_node)
    elif len(rightheap) > len(leftheap):
        move_node = heapq.heappop(rightheap)
        heapq.heappush(leftheap, -move_node)

    print(-leftheap[0])
