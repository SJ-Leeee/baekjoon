import sys
import array

count = array.array('I', [0] * 10001) 

N = int(sys.stdin.readline())
for _ in range(N):
    count[int(sys.stdin.readline())] += 1

for index, num in enumerate(count):
    if num > 0:
        for _ in range(num):
            print(index)