# sol1 : 시간 초과
# import copy
# import sys
# from collections import deque
#
#
# def find_swan():
#     for i, j in list(swan_pos):
#         board[i][j] = ","
#     while swan_pos:
#         x, y = swan_pos.popleft()
#         for dx, dy in dirs:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < R and 0 <= ny < C:
#                 if nx == swans[2] and ny == swans[3]:
#                     return True
#                 elif board[nx][ny] == ".":
#                     swan_pos.append((nx, ny))
#                     board[nx][ny] = ","
#                 elif board[nx][ny] == "X":
#                     next_pos.append((nx, ny))
#     return False
#
#
# # 입력 받기, 백조와 물 위치 저장
# R, C = map(int, sys.stdin.readline().split())
# board = []
# swans = []
# water_pos = deque()
# for i in range(R):
#     board.append(list(sys.stdin.readline().strip()))
#     for j in range(C):
#         if board[i][j] == "L":
#             swans.append(i)
#             swans.append(j)
#             water_pos.append((i, j))
#         elif board[i][j] == ".":
#             water_pos.append((i, j))
#
# # 백조 찾기 & 얼음 녹이기
# day = 0
# dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# swan_pos = deque([(swans[0], swans[1])])
# while water_pos:
#     # 백조 찾기
#     next_pos = deque()
#     if find_swan():
#         print(day)
#         break
#
#     # 얼음 녹이기
#     n = len(water_pos)
#     for i in range(n):
#         x, y = water_pos.popleft()
#         for dx, dy in dirs:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < R and 0 <= ny < C:
#                 if board[nx][ny] == "X":
#                     water_pos.append((nx, ny))
#                     board[nx][ny] = "."
#
#     swan_pos = copy.deepcopy(next_pos)
#     day += 1


# sol2
import sys
from collections import deque


def find_swan(limit):
    pos = deque([(swans[0], swans[1])])
    visited = [[False] * C for _ in range(R)]
    visited[swans[0]][swans[1]] = True
    while pos:
        x, y = pos.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                visited[nx][ny] = True
                if nx == swans[2] and ny == swans[3]:
                    return True
                elif days[nx][ny] <= limit:
                    pos.append((nx, ny))
    return False


# 입력 받기, 백조와 물 위치 저장
R, C = map(int, sys.stdin.readline().split())
board = []
swans = []
water_pos = deque()
for i in range(R):
    board.append(list(sys.stdin.readline().strip()))
    for j in range(C):
        if board[i][j] == "L":
            swans.append(i)
            swans.append(j)
            water_pos.append((i, j))
        elif board[i][j] == ".":
            water_pos.append((i, j))

# 얼음 녹는 날짜 구하기 (방문 체크 안 하면 시간 초과!)
day = 0
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
days = [[-1] * C for _ in range(R)]
for x, y in list(water_pos):
    days[x][y] = 0
while water_pos:
    n = len(water_pos)
    day += 1
    for i in range(n):
        x, y = water_pos.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and days[nx][ny] == -1:
                if board[nx][ny] == "X":
                    days[nx][ny] = day
                    water_pos.append((nx, ny))
                    board[nx][ny] = "."

# 이분 탐색으로 만날 수 있는 최단 날짜 구하기
low, high = 0, day - 1
answer = high
while low <= high:
    mid = (low + high) // 2
    if find_swan(mid):
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

print(answer)
