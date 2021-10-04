def solution(sizes):
    # x : 명함의 가로 세로 중 더 큰 값, y: 명함의 가로 세로 중 더 작은 값
    max_x = 0
    max_y = 0
    for x, y in sizes:
        if x < y:
            x, y = y, x
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y
    return max_x * max_y

# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.00ms, 10.3MB)
# 테스트 4 〉	통과 (0.00ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10.3MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)
# 테스트 8 〉	통과 (0.00ms, 10.2MB)
# 테스트 9 〉	통과 (0.00ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.02ms, 10.2MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.07ms, 10.2MB)
# 테스트 14 〉	통과 (0.14ms, 10.5MB)
# 테스트 15 〉	통과 (0.21ms, 10.4MB)
# 테스트 16 〉	통과 (0.36ms, 10.5MB)
# 테스트 17 〉	통과 (0.50ms, 10.9MB)
# 테스트 18 〉	통과 (0.54ms, 10.8MB)
# 테스트 19 〉	통과 (0.52ms, 11.4MB)
# 테스트 20 〉	통과 (0.68ms, 11.4MB)
