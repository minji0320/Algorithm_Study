# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3

def solution(number, k):
    # 뒤의 수보다 작은 값 제거 (k번 반복)
    n = len(number)
    numbers = list(map(int, number))
    for i in range(k):
        for j in range(n - 1):
            if numbers[j] == 9:
                continue
            if numbers[j] < numbers[j + 1]:
                numbers.remove(numbers[j])
                break

    return ''.join(map(str, numbers[:n - k]))

### 정확성  테스트 -> 10번 실패..
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.07ms, 10.2MB)
# 테스트 4 〉	통과 (0.27ms, 10.2MB)
# 테스트 5 〉	통과 (1.29ms, 10.3MB)
# 테스트 6 〉	통과 (263.07ms, 10.5MB)
# 테스트 7 〉	통과 (619.88ms, 13.4MB)
# 테스트 8 〉	통과 (6112.35ms, 15.3MB)
# 테스트 9 〉	통과 (120.61ms, 37MB)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	통과 (0.03ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.2MB)


### 다른 사람의 풀이
def solution2(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

### 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10MB)
# 테스트 3 〉	통과 (0.03ms, 10.1MB)
# 테스트 4 〉	통과 (0.14ms, 10.1MB)
# 테스트 5 〉	통과 (0.21ms, 10.1MB)
# 테스트 6 〉	통과 (3.52ms, 10MB)
# 테스트 7 〉	통과 (9.62ms, 10.6MB)
# 테스트 8 〉	통과 (23.28ms, 10.8MB)
# 테스트 9 〉	통과 (47.03ms, 13.8MB)
# 테스트 10 〉	통과 (118.57ms, 13.6MB)
# 테스트 11 〉	통과 (0.00ms, 10.2MB)
# 테스트 12 〉	통과 (0.00ms, 10.1MB)
