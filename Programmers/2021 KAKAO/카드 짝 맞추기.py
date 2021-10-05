from itertools import permutations
from copy import deepcopy
from collections import deque

temp_board = []

# start -> dest 까지의 최소 키 조작 횟수 구하는 함수
def bfs(start, dest):
    global temp_board
    visited = [[0] * 4 for _ in range(4)]
    dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    q = deque()
    q.append((start[0], start[1], 0))
    while q:
        x, y, move = q.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = 1
        if x == dest[0] and y == dest[1]:
            return move + 1

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                # 1칸 이동
                q.append((nx, ny, move + 1))

                # ctrl + 이동
                while True:
                    if not (0 <= nx < 4 and 0 <= ny < 4):
                        nx -= dx
                        ny -= dy
                        break
                    if temp_board[nx][ny] != 0:
                        break
                    nx += dx
                    ny += dy

                q.append((nx, ny, move + 1))


def solution(board, r, c):
    # 카드 숫자 및 위치 저장
    cards = []
    card_pos = {}
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                if board[i][j] not in cards:
                    cards.append(board[i][j])
                    card_pos[board[i][j]] = []
                card_pos[board[i][j]].append((i, j))

    # 카드 순열 구하기
    orders = list(map(list, permutations(cards, len(cards))))

    # 모든 순서를 수행하여 최소 키 조작 횟수 구하기
    global temp_board
    answer = float('inf')
    for order in orders:
        cnt = 0
        now = (r, c)
        temp_board = deepcopy(board)
        for card in order:
            # 현재 위치 -> card a, card b 까지의 거리 구하기 (a, b는 같은 종류의 카드)
            a = card_pos[card][0]
            b = card_pos[card][1]
            a_cnt = bfs(now, a)
            b_cnt = bfs(now, b)

            # 현재 위치와 더 가까운 카드로 이동 후, 나머지 카드 짝을 찾으러 이동
            if a_cnt < b_cnt:
                cnt += a_cnt
                cnt += bfs(a, b)
                now = b
            else:
                cnt += b_cnt
                cnt += bfs(b, a)
                now = a
            
            # 찾은 카드 짝 지우기
            temp_board[a[0]][a[1]] = 0
            temp_board[b[0]][b[1]] = 0

        if answer > cnt:
            answer = cnt

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.99ms, 10.4MB)
# 테스트 2 〉	통과 (1.12ms, 10.4MB)
# 테스트 3 〉	통과 (1.24ms, 10.3MB)
# 테스트 4 〉	통과 (1.87ms, 10.3MB)
# 테스트 5 〉	통과 (6.72ms, 10.4MB)
# 테스트 6 〉	통과 (8.74ms, 10.5MB)
# 테스트 7 〉	통과 (9.80ms, 10.4MB)
# 테스트 8 〉	통과 (5.27ms, 10.4MB)
# 테스트 9 〉	통과 (37.94ms, 10.4MB)
# 테스트 10 〉	통과 (50.53ms, 10.4MB)
# 테스트 11 〉	통과 (35.52ms, 10.4MB)
# 테스트 12 〉	통과 (32.36ms, 10.5MB)
# 테스트 13 〉	통과 (269.80ms, 10.6MB)
# 테스트 14 〉	통과 (246.79ms, 10.5MB)
# 테스트 15 〉	통과 (218.06ms, 10.3MB)
# 테스트 16 〉	통과 (253.54ms, 10.4MB)
# 테스트 17 〉	통과 (0.10ms, 10.3MB)
# 테스트 18 〉	통과 (0.06ms, 10.4MB)
# 테스트 19 〉	통과 (0.38ms, 10.4MB)
# 테스트 20 〉	통과 (0.25ms, 10.3MB)
# 테스트 21 〉	통과 (4.69ms, 10.4MB)
# 테스트 22 〉	통과 (247.94ms, 10.4MB)
# 테스트 23 〉	통과 (217.25ms, 10.5MB)
# 테스트 24 〉	통과 (5.77ms, 10.3MB)
# 테스트 25 〉	통과 (236.08ms, 10.4MB)
# 테스트 26 〉	통과 (5.84ms, 10.4MB)
# 테스트 27 〉	통과 (5.28ms, 10.4MB)
# 테스트 28 〉	통과 (1.24ms, 10.4MB)
# 테스트 29 〉	통과 (2.10ms, 10.4MB)
# 테스트 30 〉	통과 (1.05ms, 10.3MB)
