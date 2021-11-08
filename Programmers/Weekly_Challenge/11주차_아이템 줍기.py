# from collections import deque
#
# # 실패한 소스
# def solution(rectangle, characterX, characterY, itemX, itemY):
#     # 사각형 테두리 위치 저장
#     board = {}
#     for idx, rect in enumerate(rectangle):
#         min_x, min_y, max_x, max_y = rect
#         for x in range(min_x, max_x + 1):
#             if (x, min_y) not in board:
#                 board[(x, min_y)] = [idx]
#             else:
#                 board[(x, min_y)].append(idx)
#
#             if (x, max_y) not in board:
#                 board[(x, max_y)] = [idx]
#             else:
#                 board[(x, max_y)].append(idx)
#
#         for y in range(min_y + 1, max_y):
#             if (min_x, y) not in board:
#                 board[(min_x, y)] = [idx]
#             else:
#                 board[(min_x, y)].append(idx)
#
#             if (max_x, y) not in board:
#                 board[(max_x, y)] = [idx]
#             else:
#                 board[(max_x, y)].append(idx)
#
#     # 시작 지점에서 두 가지 방향으로 이동
#     # q : 이동횟수, 현재 x 좌표, 현재 y 좌표, 현재 사각형, 다음 사각형, 이동 방향
#     visited = [[False] * 51 for _ in range(51)]
#     dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
#     x, y = characterX, characterY
#     visited[x][y] = True
#     q = deque()
#     for i in range(4):
#         nx, ny = x + dirs[i][0], y + dirs[i][1]
#         if 0 <= nx < 51 and 0 <= ny < 51:
#             for j in range(len(board[(x, y)])):
#                 if (nx, ny) in board and board[(x, y)][j] in board[(nx, ny)]:
#                     if len(board[(nx, ny)]) == 1:
#                         q.append((1, nx, ny, board[(x, y)][j], board[(nx, ny)][j], i))
#                     else:
#                         for rect in board[(nx, ny)]:
#                             if rect != board[(x, y)][j]:
#                                 q.append((1, nx, ny, board[(x, y)][j], rect, i))
#
#     # 두 방향으로 이동하며 가장 먼저 item 발견할때까지의 거리 구하기
#     while q:
#         cnt, x, y, now_rect, next_rect, start_dir = q.popleft()
#         visited[x][y] = True
#
#         # 아이템을 발견한 경우
#         if x == itemX and y == itemY:
#             return cnt
#
#         for i in range(start_dir, start_dir + 4):
#             nx, ny = x + dirs[i % 4][0], y + dirs[i % 4][1]
#             if 0 <= nx < 51 and 0 <= ny < 51 and not visited[nx][ny] and (nx, ny) in board:
#                 # 같은 사각형 테두리로 이동하는 경우
#                 if now_rect == next_rect and now_rect in board[(nx, ny)]:
#                     if len(board[(nx, ny)]) == 1:
#                         # 같은 테두리 -> 같은 테두리
#                         q.append((cnt + 1, nx, ny, now_rect, now_rect, i % 4))
#                         break
#                     else:
#                         # 같은 테두리 -> 다른 테두리
#                         for rect in board[(nx, ny)]:
#                             if rect != now_rect:
#                                 q.append((cnt + 1, nx, ny, now_rect, rect, i % 4))
#                                 break
#
#                 # 다른 사각형 테두리로 이동하는 경우
#                 elif now_rect != next_rect and next_rect in board[(nx, ny)]:
#                     min_x, min_y, max_x, max_y = rectangle[now_rect]
#                     # 현재 사각형에서 벗어나야 함
#                     if min_x <= nx <= max_x and min_y <= ny <= max_y:
#                         continue
#
#                     if len(board[(nx, ny)]) == 1:
#                         # 다른 테두리 -> 같은 테두리
#                         q.append((cnt + 1, nx, ny, next_rect, board[(nx, ny)][0], i % 4))
#                         break
#                     else:
#                         # 다른 테두리 -> 다른 테두리
#                         for rect in board[(nx, ny)]:
#                             if rect != next_rect:
#                                 q.append((cnt + 1, nx, ny, next_rect, rect, i % 4))
#                         break

# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.5MB)
# 테스트 2 〉	통과 (0.04ms, 10.6MB)
# 테스트 3 〉	통과 (0.03ms, 10.5MB)
# 테스트 4 〉	통과 (0.03ms, 10.5MB)
# 테스트 5 〉	통과 (0.03ms, 10.6MB)
# 테스트 6 〉	통과 (0.05ms, 10.5MB)
# 테스트 7 〉	통과 (0.05ms, 10.4MB)
# 테스트 8 〉	통과 (0.09ms, 10.5MB)
# 테스트 9 〉	통과 (0.18ms, 10.6MB)
# 테스트 10 〉	통과 (0.24ms, 10.3MB)
# 테스트 11 〉	통과 (0.30ms, 10.5MB)
# 테스트 12 〉	통과 (0.17ms, 10.6MB)
# 테스트 13 〉	실패 (런타임 에러)
# 테스트 14 〉	통과 (0.16ms, 10.5MB)
# 테스트 15 〉	통과 (0.07ms, 10.4MB)
# 테스트 16 〉	통과 (0.25ms, 10.4MB)
# 테스트 17 〉	통과 (0.32ms, 10.4MB)
# 테스트 18 〉	실패 (0.27ms, 10.4MB)
# 테스트 19 〉	통과 (0.30ms, 10.5MB)
# 테스트 20 〉	통과 (0.26ms, 10.5MB)
# 테스트 21 〉	통과 (0.37ms, 10.6MB)
# 테스트 22 〉	실패 (0.24ms, 10.5MB)
# 테스트 23 〉	통과 (0.32ms, 10.6MB)
# 테스트 24 〉	실패 (런타임 에러)
# 테스트 25 〉	통과 (0.17ms, 10.5MB)
# 테스트 26 〉	실패 (런타임 에러)
# 테스트 27 〉	통과 (0.18ms, 10.5MB)
# 테스트 28 〉	실패 (런타임 에러)
# 테스트 29 〉	실패 (런타임 에러)
# 테스트 30 〉	실패 (런타임 에러)
# 채점 결과
# 정확성: 75.7
# 합계: 75.7 / 100.0

import numpy as np
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 사각형 테두리 위치 저장
    board = {}
    rectangle = np.array(rectangle)
    rectangle *= 2
    for idx, rect in enumerate(rectangle):
        min_x, min_y, max_x, max_y = rect
        for x in range(min_x, max_x + 1):
            if (x, min_y) not in board:
                board[(x, min_y)] = [idx]
            else:
                board[(x, min_y)].append(idx)

            if (x, max_y) not in board:
                board[(x, max_y)] = [idx]
            else:
                board[(x, max_y)].append(idx)

        for y in range(min_y + 1, max_y):
            if (min_x, y) not in board:
                board[(min_x, y)] = [idx]
            else:
                board[(min_x, y)].append(idx)

            if (max_x, y) not in board:
                board[(max_x, y)] = [idx]
            else:
                board[(max_x, y)].append(idx)

    # 시작 지점에서 두 가지 방향으로 이동
    # q : 이동횟수, 현재 x 좌표, 현재 y 좌표, 현재 사각형
    visited = [[False] * 101 for _ in range(101)]
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    x, y = characterX * 2, characterY * 2
    visited[x][y] = True
    q = deque()
    for rect in board[(x, y)]:
        q.append((0, x, y, rect))

    # 두 방향으로 이동하며 가장 먼저 item 발견할때까지의 거리 구하기
    while q:
        cnt, x, y, now_rect = q.popleft()

        # 아이템을 발견한 경우
        if x == itemX * 2 and y == itemY * 2:
            return cnt

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 101 and 0 <= ny < 101 and not visited[nx + dx][ny + dy] and (nx, ny) in board:
                # 현재 위치 : 테두리가 겹치지 않는 곳
                if len(board[(x, y)]) == 1:
                    if board[(x, y)][0] in board[(nx, ny)]:
                        q.append((cnt + 1, nx + dx, ny + dy, board[(x, y)][0]))
                        visited[nx + dx][ny + dy] = True

                # 현재 위치 : 테두리가 겹치는 곳
                else:
                    if board[(x, y)][1] in board[(nx, ny)]:
                        # 현재 사각형에서 벗어나야 함
                        min_x, min_y, max_x, max_y = rectangle[board[(x, y)][0]]
                        if min_x <= nx <= max_x and min_y <= ny <= max_y:
                            continue
                        q.append((cnt + 1, nx + dx, ny + dy, board[(x, y)][1]))
                        visited[nx + dx][ny + dy] = True
                    if board[(x, y)][0] in board[(nx, ny)]:
                        # 현재 사각형에서 벗어나야 함
                        min_x, min_y, max_x, max_y = rectangle[board[(x, y)][1]]
                        if min_x <= nx <= max_x and min_y <= ny <= max_y:
                            continue
                        q.append((cnt + 1, nx + dx, ny + dy, board[(x, y)][0]))
                        visited[nx + dx][ny + dy] = True
