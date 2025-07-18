import sys


blue = 0
white = 0


def count_paper(paper_list, r):
    global white, blue

    half = r // 2

    list_sum = 0
    for i in range(r):
        list_sum += sum(paper_list[i])

    if list_sum == 0:
        white += 1
        return

    if list_sum == r**2:
        blue += 1
        return

    half = r // 2

    q1 = [row[half:] for row in paper_list[:half]]
    q2 = [row[:half] for row in paper_list[:half]]
    q3 = [row[:half] for row in paper_list[half:]]
    q4 = [row[half:] for row in paper_list[half:]]

    count_paper(q1, half)
    count_paper(q2, half)
    count_paper(q3, half)
    count_paper(q4, half)

    return


N = int(sys.stdin.readline())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

count_paper(data, N)

print(white)
print(blue)
