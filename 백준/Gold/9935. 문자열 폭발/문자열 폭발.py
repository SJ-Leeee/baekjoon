
import sys


input_string = sys.stdin.readline().strip()
find_string = sys.stdin.readline().strip()
last_string = find_string[-1]
data = list(input_string)

stack = []
for i in range(len(data)):
    stack.append(data[i])
    if data[i] == last_string and len(stack) >= len(find_string):
        if find_string == "".join(stack[-len(find_string) :]):
            for _ in range(len(find_string)):
                stack.pop()


if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
