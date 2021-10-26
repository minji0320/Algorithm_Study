import sys
from collections import Counter
N = int(sys.stdin.readline())
cards = []
for i in range(N):
    cards.append(int(sys.stdin.readline()))
print(sorted(Counter(cards).items(), key=lambda x: (-x[1], x[0]))[0][0])
