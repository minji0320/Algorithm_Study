def solution(enroll, referral, seller, amount):
    # 소개인 정보 저장, 이익금 초기화
    recommenders = {}
    profits = {}
    for i, employee in enumerate(enroll):
        recommenders[employee] = referral[i]
        profits[employee] = 0

    # 판매 수익 분배하기
    for i, employee in enumerate(seller):
        now = employee
        profit = amount[i] * 100
        while now in recommenders and profit > 0:
            recommender = recommenders[now]
            distribution = profit // 10
            profits[now] += profit - distribution
            now = recommender
            profit = distribution

    # 총 이익금 구하기
    answer = []
    for employee in enroll:
        answer.append(profits[employee])

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.07ms, 10.3MB)
# 테스트 3 〉	통과 (0.04ms, 10.3MB)
# 테스트 4 〉	통과 (0.11ms, 10.3MB)
# 테스트 5 〉	통과 (0.83ms, 10.4MB)
# 테스트 6 〉	통과 (2.53ms, 12.7MB)
# 테스트 7 〉	통과 (2.82ms, 12.6MB)
# 테스트 8 〉	통과 (6.28ms, 12.7MB)
# 테스트 9 〉	통과 (14.23ms, 14.1MB)
# 테스트 10 〉	통과 (114.57ms, 21.2MB)
# 테스트 11 〉	통과 (96.51ms, 20.5MB)
# 테스트 12 〉	통과 (95.38ms, 20.6MB)
# 테스트 13 〉	통과 (97.77ms, 20.6MB)
