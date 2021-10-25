import sys

N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
result = [cost[0][i] for i in range(3)]

for i in range(1, N):
    r = cost[i][0] + min(result[1], result[2])
    g = cost[i][1] + min(result[0], result[2])
    b = cost[i][2] + min(result[0], result[1])
    result = [r, g, b]

print(min(result))
