import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
answer = 0
for i in range(N):
    answer += arr[i] * (N - i)

print(answer)