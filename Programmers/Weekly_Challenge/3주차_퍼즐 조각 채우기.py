def solution(game_board, table):
    n = len(game_board)
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    pieces = {}

    # type : 1 퍼즐 조각 찾기, 0 게임 보드 빈칸 찾기
    def get_position(i, j, type):
        cnt = 1
        pos = []
        temp_pos = []

        if type == 1:
            table[i][j] = -1
            pos.append([0, 0])
        else:
            game_board[i][j] = -1
            pos.append([i, j])

        temp_pos.append([i, j])

        while len(temp_pos) != 0:
            x, y = temp_pos.pop()
            for a in range(4):
                nx, ny = x + dx[a], y + dy[a]
                if 0 <= nx < n and 0 <= ny < n:
                    if type == 1 and table[nx][ny] == 1:
                        cnt += 1
                        table[nx][ny] = -1
                        pos.append([nx - i, ny - j])
                        temp_pos.append([nx, ny])
                    elif type == 0 and game_board[nx][ny] == 0:
                        cnt += 1
                        game_board[nx][ny] = -1
                        pos.append([nx, ny])
                        temp_pos.append([nx, ny])
        return cnt, pos

    def rotate(piece):
        return [[-y, x] for x, y in piece]

    # 퍼즐 조각 저장
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                cnt, pieces_pos = get_position(i, j, 1)

                if cnt not in pieces:
                    pieces[cnt] = []
                pieces[cnt].append(pieces_pos)

    # 게임 보드 빈칸에 퍼즐 조각 채우기
    answer = 0
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                cnt, blank_pos = get_position(i, j, 0)
                blank_pos.sort()

                if cnt not in pieces:
                    continue

                for piece in pieces[cnt]:
                    is_right = False
                    rotated = piece
                    for start_i, start_j in blank_pos:
                        for _ in range(4):
                            temp_pos = [[start_i + pi, start_j + pj] for pi, pj in rotated]
                            if blank_pos == sorted(temp_pos):
                                answer += cnt
                                pieces[cnt].remove(piece)
                                is_right = True
                                break
                            rotated = rotate(rotated)
                        if is_right:
                            break
                    if is_right:
                        break

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.18ms, 10.3MB)
# 테스트 2 〉	통과 (0.16ms, 10.3MB)
# 테스트 3 〉	통과 (0.31ms, 10.3MB)
# 테스트 4 〉	통과 (0.23ms, 10.4MB)
# 테스트 5 〉	통과 (0.19ms, 10.3MB)
# 테스트 6 〉	통과 (5.67ms, 10.3MB)
# 테스트 7 〉	통과 (2.85ms, 10.4MB)
# 테스트 8 〉	통과 (2.73ms, 10.4MB)
# 테스트 9 〉	통과 (3.18ms, 10.3MB)
# 테스트 10 〉	통과 (31.29ms, 10.3MB)
# 테스트 11 〉	통과 (2.89ms, 10.3MB)
# 테스트 12 〉	통과 (12.82ms, 10.4MB)
# 테스트 13 〉	통과 (14.21ms, 10.3MB)
# 테스트 14 〉	통과 (0.13ms, 10.3MB)
# 테스트 15 〉	통과 (0.04ms, 10.3MB)
# 테스트 16 〉	통과 (0.08ms, 10.2MB)
# 테스트 17 〉	통과 (0.08ms, 10.2MB)
# 테스트 18 〉	통과 (0.09ms, 10.3MB)
# 테스트 19 〉	통과 (0.04ms, 10.3MB)
# 테스트 20 〉	통과 (0.05ms, 10.2MB)
# 테스트 21 〉	통과 (0.03ms, 10.2MB)
# 테스트 22 〉	통과 (0.06ms, 10.3MB)