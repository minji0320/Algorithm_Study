import sys

N, K = map(int, sys.stdin.readline().split())
ices = {}
for _ in range(N):
    g, x = map(int, sys.stdin.readline().split())
    ices[x] = g
sorted_ices = sorted(ices.items())

end = sorted_ices[0][0]
max_ices = 0
now_ices = 0
for start, _ in sorted_ices:
    while end < sorted_ices[-1][0] + 1 and end - start <= K * 2:
        if end in ices:
            now_ices += ices[end]
        end += 1
    if max_ices < now_ices:
        max_ices = now_ices
    now_ices -= ices[start]

print(max_ices)
