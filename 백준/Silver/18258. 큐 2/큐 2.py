from collections import deque
import sys

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.


def queue_action(command, dq):
    if command[0] == "push":
        dq.append(int(command[1]))
    elif command[0] == "pop":
        if len(dq) == 0:
            return -1
        else:
            return dq.popleft()
    elif command[0] == "size":
        return len(dq)
    elif command[0] == "empty":
        if len(dq) == 0:
            return 1
        else:
            return 0
    elif command[0] == "front":
        if len(dq) == 0:
            return -1
        else:
            return dq[0]
    elif command[0] == "back":
        if len(dq) == 0:
            return -1
        else:
            return dq[-1]


dq = deque()
# dq.append(1)  # 오른쪽 끝에 추가
# dq.appendleft(2)  # 왼쪽 끝에 추가
# # dq.pop()  # 오른쪽 끝에서 제거
# print(dq.popleft())  # 왼쪽 끝에서 제거 (FIFO)
# print(dq.popleft())  # 왼쪽 끝에서 제거 (FIFO)
# print(dq.popleft())  # 왼쪽 끝에서 제거 (FIFO)

N = int(sys.stdin.readline())

for _ in range(N):
    command = sys.stdin.readline().split()
    a = queue_action(command, dq)
    if a != None:
        print(a)
