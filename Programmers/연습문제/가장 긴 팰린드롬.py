def solution(s):
    n = len(s)
    answer = 1
    for start in range(n):
        for end in range(start + 2, n + 1):
            rev_s = s[start:end]
            if len(rev_s) < answer:
                continue
            if rev_s == rev_s[::-1]:
                answer = max(answer, end - start)

    return answer
