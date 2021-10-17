from itertools import combinations


def solution(places):
    answer = []
    for place in places:
        # P 위치 저장
        p_pos = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    p_pos.append((i, j))

        # P 2명씩 조합하여 거리두기 여부 체크
        is_right = True
        comb = list(combinations(p_pos, 2))
        for a, b in comb:
            diff_x, diff_y = b[0] - a[0], b[1] - a[1]
            abs_x, abs_y = abs(diff_x), abs(diff_y)
            distance = abs_x + abs_y

            if distance == 1:
                is_right = False
                break
            if distance == 2:
                # 칸막이 여부 체크
                if abs_x == abs_y:
                    if place[a[0] + diff_x][a[1]] != "X" or place[a[0]][a[1] + diff_y] != "X":
                        is_right = False
                        break
                elif abs_x > abs_y:
                    if place[a[0] + int(diff_x/2)][a[1]] != "X":
                        is_right = False
                        break
                else:
                    if place[a[0]][a[1] + int(diff_y/2)] != "X":
                        is_right = False
                        break

        if is_right:
            answer.append(1)
        else:
            answer.append(0)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.11ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.04ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.05ms, 10.3MB)
# 테스트 7 〉	통과 (0.03ms, 10.3MB)
# 테스트 8 〉	통과 (0.04ms, 10.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.3MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 테스트 11 〉	통과 (0.03ms, 10.3MB)
# 테스트 12 〉	통과 (0.04ms, 10.4MB)
# 테스트 13 〉	통과 (0.05ms, 10.3MB)
# 테스트 14 〉	통과 (0.04ms, 10.3MB)
# 테스트 15 〉	통과 (0.03ms, 10.3MB)
# 테스트 16 〉	통과 (0.03ms, 10.3MB)
# 테스트 17 〉	통과 (0.03ms, 10.3MB)
# 테스트 18 〉	통과 (0.04ms, 10.3MB)
# 테스트 19 〉	통과 (0.05ms, 10.4MB)
# 테스트 20 〉	통과 (0.04ms, 10.3MB)
# 테스트 21 〉	통과 (0.07ms, 10.3MB)
# 테스트 22 〉	통과 (0.03ms, 10.4MB)
# 테스트 23 〉	통과 (0.02ms, 10.4MB)
# 테스트 24 〉	통과 (0.11ms, 10.3MB)
# 테스트 25 〉	통과 (0.02ms, 10.3MB)
# 테스트 26 〉	통과 (0.04ms, 10.3MB)
# 테스트 27 〉	통과 (0.03ms, 10.3MB)
# 테스트 28 〉	통과 (0.02ms, 10.3MB)
# 테스트 29 〉	통과 (0.03ms, 10.3MB)
# 테스트 30 〉	통과 (0.02ms, 10.4MB)
