import sys

rl = sys.stdin.readline
N = int(rl())
arr = list(zip(map(int, rl().split(" ")), range(N)))
arr.sort()

answer = [0] * N
max_num, cnt = arr[0][0], 0
for i in range(N):
    if max_num < arr[i][0]:
        max_num = arr[i][0]
        cnt += 1
    answer[arr[i][1]] = str(cnt)

print(" ".join(answer))
