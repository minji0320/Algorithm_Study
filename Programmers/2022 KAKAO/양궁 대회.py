import copy

max_diff = 0
answer = [0 for _ in range(11)]


def solution(n, info):
    global max_diff, answer

    def dfs(idx, cnt, result):
        global max_diff, answer
        if cnt > n or idx > 10:
            return
        if idx == 10:
            result[idx] = n - cnt
            cnt = n
        if cnt == n:
            a, b = 0, 0
            for i in range(11):
                if info[i] != 0 and info[i] >= result[i]:
                    a += 10 - i
                elif info[i] < result[i]:
                    b += 10 - i
            if max_diff < b - a:
                max_diff = b - a
                answer = copy.deepcopy(result)
            elif max_diff != 0 and max_diff == b - a:
                print(answer)
                print(result)
                print(max_diff)
                for j in range(10, -1, -1):
                    if result[j] < answer[j]:
                        break
                    elif result[j] > answer[j]:
                        answer = copy.deepcopy(result)
                        break
            return

        dfs(idx + 1, cnt, copy.deepcopy(result))
        result[idx] = choices[idx]
        dfs(idx + 1, cnt + choices[idx], copy.deepcopy(result))

    choices = []
    for i in range(11):
        choices.append(info[i] + 1)

    dfs(0, 0, copy.deepcopy(answer))
    if sum(answer) == 0:
        answer = [-1]
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.56ms, 10.3MB)
# 테스트 2 〉	통과 (7.43ms, 10.3MB)
# 테스트 3 〉	통과 (8.95ms, 10.4MB)
# 테스트 4 〉	통과 (3.51ms, 10.4MB)
# 테스트 5 〉	통과 (8.64ms, 10.4MB)
# 테스트 6 〉	통과 (8.19ms, 10.4MB)
# 테스트 7 〉	통과 (3.06ms, 10.4MB)
# 테스트 8 〉	통과 (1.66ms, 10.3MB)
# 테스트 9 〉	통과 (5.66ms, 10.3MB)
# 테스트 10 〉	통과 (1.21ms, 10.3MB)
# 테스트 11 〉	통과 (2.48ms, 10.3MB)
# 테스트 12 〉	통과 (2.09ms, 10.3MB)
# 테스트 13 〉	통과 (11.00ms, 10.4MB)
# 테스트 14 〉	통과 (7.32ms, 10.2MB)
# 테스트 15 〉	통과 (8.82ms, 10.3MB)
# 테스트 16 〉	통과 (4.38ms, 10.3MB)
# 테스트 17 〉	통과 (4.07ms, 10.3MB)
# 테스트 18 〉	통과 (1.10ms, 10.3MB)
# 테스트 19 〉	통과 (0.15ms, 10.3MB)
# 테스트 20 〉	통과 (8.51ms, 10.3MB)
# 테스트 21 〉	통과 (7.64ms, 10.3MB)
# 테스트 22 〉	통과 (10.82ms, 10.3MB)
# 테스트 23 〉	통과 (1.39ms, 10.4MB)
# 테스트 24 〉	통과 (11.19ms, 10.2MB)
# 테스트 25 〉	통과 (12.67ms, 10.3MB)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0
