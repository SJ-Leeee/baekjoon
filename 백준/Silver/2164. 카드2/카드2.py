
from collections import deque
import sys

N = int(sys.stdin.readline())
dq = deque()
dq.extend(range(1, N + 1))

while True:
    if len(dq) == 1:
        break
    dq.popleft()
    if len(dq) == 1:
        break
    dq.append(dq.popleft())

print(dq[0])
