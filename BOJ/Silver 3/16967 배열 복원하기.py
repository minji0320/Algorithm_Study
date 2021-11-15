import sys

H, W, X, Y = map(int, sys.stdin.readline().split())
B = []
for i in range(H + X):
    B.append(list(map(int, sys.stdin.readline().split())))

A = []
for i in range(H):
    A.append([])
    for j in range(W):
        A[i].append(B[i][j])
        B[i + X][j + Y] = B[i + X][j + Y] - A[i][j]

for i in range(H):
    print(" ".join(map(str, A[i])))
