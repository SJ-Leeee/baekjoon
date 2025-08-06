
import sys


data = sys.stdin.readline().strip()


n_sum = 0
last_char = 0
flag = False
for i in range(len(data)):
    if data[i] == "+":
        number = -int(data[last_char:i]) if flag else int(data[last_char:i])
        n_sum += number
        last_char = i + 1
    elif data[i] == "-":
        number = int(data[last_char:i])
        if not flag:
            n_sum += number
            flag = True
        else:
            n_sum -= number
        last_char = i + 1

n_sum += -int(data[last_char:]) if flag else int(data[last_char:])

print(n_sum)