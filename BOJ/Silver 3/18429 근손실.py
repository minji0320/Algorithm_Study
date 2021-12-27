import sys
from itertools import permutations


def is_right(weights):
    now = 500
    for weight in weights:
        now += weight - K
        if now < 500:
            return False

    return True


N, K = map(int, sys.stdin.readline().split())
kits = list(map(int, sys.stdin.readline().split()))

orders = list(permutations(kits, N))
answer = 0
for order in orders:
    if is_right(order):
        answer += 1

print(answer)
