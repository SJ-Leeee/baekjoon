from collections import deque
import heapq
import sys

N = int(sys.stdin.readline())

for _ in range(N):
    data_num, find_idx = map(int, sys.stdin.readline().split())
    priority_data = list(map(int, sys.stdin.readline().split()))
    origin_data = deque()  # 우선순위와 인덱스를 가진 배열
    heap_data = []
    for idx, item in enumerate(priority_data):
        item = -item  # 음수화
        heap_data.append(item)  # 힙데이터에도 삽입
        origin_data.append([idx, item])
    heapq.heapify(heap_data)

    count = 1

    while len(origin_data) > 0:

        data = origin_data.popleft()
        if heap_data[0] == data[1]:
            if find_idx == data[0]:
                break
            heapq.heappop(heap_data)  # 가장 큰 우선순위를 날려버림
            count += 1
        else:  # 같지 않으면
            origin_data.append(data)  # 다시 뒤로

    print(count)