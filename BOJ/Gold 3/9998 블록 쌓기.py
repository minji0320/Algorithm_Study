import sys


def count(height):
    cnt = 0
    for i in range(N):
        cnt += abs(Y[i] - (height + abs(N // 2 - i)))
        cnt += abs(D[i] - (height + abs(N // 2 - i)))
    return cnt


N = int(sys.stdin.readline())
Y = list(map(int, sys.stdin.readline().split()))
D = list(map(int, sys.stdin.readline().split()))

low, high = 0, 10 ** 12 - N // 2
low_cnt, high_cnt = count(low), count(high)
while low < high:
    mid = (low + high) // 2
    if low_cnt < high_cnt:
        high = mid
        high_cnt = count(high)
    else:
        low = mid + 1
        low_cnt = count(low)

print(low_cnt)

# 참고 사이트
# https://ws-pace.tistory.com/214
