import sys

R, C, N = map(int, sys.stdin.readline().split())

board = [[]]
empty = [['.'] * C for _ in range(R)]
full = [['O'] * C for _ in range(R)]
for i in range(R):
    board[0].append(sys.stdin.readline().strip())

if N == 1:
    for i in range(R):
        print("".join(board[0][i]))
elif N % 2 == 0:
    for i in range(R):
        print("".join(full[i]))
else:
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(N//2):
        temp = [item[:] for item in full]
        for x in range(R):
            for y in range(C):
                if board[-1][x][y] == 'O':
                    temp[x][y] = '.'
                    for k in range(4):
                        nx, ny = x + dirs[k][0], y + dirs[k][1]
                        if 0 <= nx < R and 0 <= ny < C:
                            temp[nx][ny] = '.'

        if len(board) > 1 and temp == board[-2]:
            left = N//2 - i - 1
            if left % 2 == 0:
                board.append(temp)
                break
            else:
                break

        board.append(temp)

    for i in range(R):
        print("".join(board[-1][i]))
