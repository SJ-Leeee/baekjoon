import sys


N = int(sys.stdin.readline())
meeting_room = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meeting_room.append((start, end))


meeting_room.sort(key=lambda x: (x[1], x[0]))


recent_end = meeting_room[0][1]
cnt = 1
for i in range(1, N):
    if meeting_room[i][0] >= recent_end:
        cnt += 1
        recent_end = meeting_room[i][1]

print(cnt)
