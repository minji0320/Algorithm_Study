# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations


def solution(orders, course):
    answer = []
    for cnt in course:
        course_candidates = []
        course_cnt = {}
        # 코스 메뉴 조합 & 주문 횟수 구하기
        for order in orders:
            course_candidates += list(map("".join, combinations(sorted(order), cnt)))
        for candidate in course_candidates:
            if candidate not in course_cnt:
                course_cnt[candidate] = 0
            course_cnt[candidate] += 1

        # 최다 주문량 코스메뉴 저장
        max = 0
        temp = []
        for course, cnt in course_cnt.items():
            if cnt >= 2 and cnt > max:
                max = cnt
                temp = [course]
            elif cnt == max:
                temp.append(course)

        answer += temp

    return sorted(answer)

# 정확성  테스트
# 테스트 1 〉	통과 (0.12ms, 10.2MB)
# 테스트 2 〉	통과 (0.07ms, 10.3MB)
# 테스트 3 〉	통과 (0.11ms, 10.3MB)
# 테스트 4 〉	통과 (0.13ms, 10.2MB)
# 테스트 5 〉	통과 (0.14ms, 10.2MB)
# 테스트 6 〉	통과 (0.33ms, 10.2MB)
# 테스트 7 〉	통과 (0.31ms, 10.2MB)
# 테스트 8 〉	통과 (1.97ms, 10.3MB)
# 테스트 9 〉	통과 (1.02ms, 10.4MB)
# 테스트 10 〉	통과 (1.24ms, 10.4MB)
# 테스트 11 〉	통과 (1.18ms, 10.3MB)
# 테스트 12 〉	통과 (1.03ms, 10.3MB)
# 테스트 13 〉	통과 (1.56ms, 10.4MB)
# 테스트 14 〉	통과 (1.41ms, 10.4MB)
# 테스트 15 〉	통과 (1.37ms, 10.4MB)
# 테스트 16 〉	통과 (0.52ms, 10.3MB)
# 테스트 17 〉	통과 (0.30ms, 10.2MB)
# 테스트 18 〉	통과 (0.17ms, 10.2MB)
# 테스트 19 〉	통과 (0.05ms, 10.2MB)
# 테스트 20 〉	통과 (0.44ms, 10.3MB)