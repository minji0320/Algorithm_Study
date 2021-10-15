from itertools import combinations


def solution(line):
    # 직선 2개씩 조합 만들기
    comb = list(combinations(line, 2))

    # 직선 조합에서 교점 찾기
    min_x, min_y, max_x, max_y = float("inf"), float("inf"), float("-inf"), float("-inf")
    intersection = set()
    for a, b in comb:
        A, B, C, D, E, F = a[0], a[1], b[0], b[1], a[2], b[2]
        if A * D - B * C == 0:
            continue
        else:
            # 정수인 교점 구하기
            x = (B * F - E * D) / (A * D - B * C)
            y = (E * C - A * F) / (A * D - B * C)
            if x - int(x) != 0 or y - int(y) != 0:
                continue
            intersection.add((int(x), int(y)))

            # 최소/최대 좌표 구하기
            if min_x > x:
                min_x = x
            if min_y > y:
                min_y = y
            if max_x < x:
                max_x = x
            if max_y < y:
                max_y = y
    min_x, min_y, max_x, max_y = int(min_x), int(min_y), int(max_x), int(max_y)

    # 모든 교점을 포함하는 최소 사각형 그리기
    answer = []
    for i in range(max_y - min_y + 1):
        answer.append("")
        for j in range(max_x - min_x + 1):
            print(i, j, min_x, min_y)
            if (j + min_x, i + min_y) in intersection:
                answer[i] += "*"
            else:
                answer[i] += "."
    answer.reverse()
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.99ms, 10.3MB)
# 테스트 2 〉	통과 (66.15ms, 11.2MB)
# 테스트 3 〉	통과 (0.26ms, 10.3MB)
# 테스트 4 〉	통과 (107.75ms, 12.3MB)
# 테스트 5 〉	통과 (29.97ms, 10.7MB)
# 테스트 6 〉	통과 (9.21ms, 10.4MB)
# 테스트 7 〉	통과 (36.13ms, 11MB)
# 테스트 8 〉	통과 (0.17ms, 10.3MB)
# 테스트 9 〉	통과 (311.47ms, 32.5MB)
# 테스트 10 〉	통과 (314.98ms, 33.9MB)
# 테스트 11 〉	통과 (395.62ms, 38.1MB)
# 테스트 12 〉	통과 (461.85ms, 42.7MB)
# 테스트 13 〉	통과 (483.07ms, 43.5MB)
# 테스트 14 〉	통과 (442.90ms, 39.2MB)
# 테스트 15 〉	통과 (406.80ms, 39.4MB)
# 테스트 16 〉	통과 (350.80ms, 35.7MB)
# 테스트 17 〉	통과 (425.38ms, 39.1MB)
# 테스트 18 〉	통과 (385.88ms, 38.5MB)
# 테스트 19 〉	통과 (371.72ms, 38.1MB)
# 테스트 20 〉	통과 (301.84ms, 32.7MB)
# 테스트 21 〉	통과 (341.55ms, 33.2MB)
# 테스트 22 〉	통과 (0.09ms, 10.3MB)
# 테스트 23 〉	통과 (0.05ms, 10.3MB)
# 테스트 24 〉	통과 (0.02ms, 10.2MB)
# 테스트 25 〉	통과 (0.07ms, 10.3MB)
# 테스트 26 〉	통과 (0.10ms, 10.3MB)
# 테스트 27 〉	통과 (0.01ms, 10.3MB)
# 테스트 28 〉	통과 (0.02ms, 10.3MB)
# 테스트 29 〉	통과 (0.01ms, 10.2MB)
