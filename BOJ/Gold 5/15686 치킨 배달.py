import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

home = []
chicken = []
for i in range(N):
	temp = sys.stdin.readline().split()
	for j in range(N):
		if temp[j] == "1":
			home.append((i, j))
		elif temp[j] == "2":
			chicken.append((i, j))

combs = combinations(chicken, M)
answer = float("inf")
for comb in combs:
	total_dist = 0
	for h in home:
		min_dist = float("inf")
		for c in comb:
			temp_dist = abs(h[0] - c[0]) + abs(h[1] - c[1])
			if temp_dist < min_dist:
				min_dist = temp_dist
		total_dist += min_dist
	if total_dist < answer:
		answer = total_dist

print(answer)
