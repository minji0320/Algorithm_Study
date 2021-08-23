# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

def solution(numbers, target):
    result = [0]
    for num in numbers:
        temp = []
        for r in result:
            temp.append(r + num)
            temp.append(r - num)
        result = temp

    return result.count(target)

### 정확성  테스트
# 테스트 1 〉	통과 (159.41ms, 50MB)
# 테스트 2 〉	통과 (157.49ms, 49.4MB)
# 테스트 3 〉	통과 (0.14ms, 10MB)
# 테스트 4 〉	통과 (0.57ms, 10.4MB)
# 테스트 5 〉	통과 (4.46ms, 11.1MB)
# 테스트 6 〉	통과 (0.30ms, 10.2MB)
# 테스트 7 〉	통과 (0.14ms, 9.99MB)
# 테스트 8 〉	통과 (1.15ms, 10.3MB)