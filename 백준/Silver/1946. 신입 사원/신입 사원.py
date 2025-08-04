import sys


N = int(sys.stdin.readline())
for _ in range(N):
    p_N = int(sys.stdin.readline())
    people_grade = []
    for _ in range(p_N):
        r1, r2 = map(int, sys.stdin.readline().split())
        people_grade.append((r1, r2))

    people_grade.sort()

    cnt = 1
    min_interview = people_grade[0][1]
    for i in range(1, len(people_grade)):
        if people_grade[i][1] < min_interview:
            cnt += 1
            min_interview = people_grade[i][1]

    print(cnt)
