import sys

N, K = map(int, sys.stdin.readline().split())
items = [[0, 0]]
for i in range(N):
    items.append(list(map(int, sys.stdin.readline().split())))

result = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j - items[i][0] >= 0:
            result[i][j] = max(result[i - 1][j - items[i][0]] + items[i][1], result[i - 1][j])
        else:
            result[i][j] = result[i - 1][j]

print(result[-1][-1])
