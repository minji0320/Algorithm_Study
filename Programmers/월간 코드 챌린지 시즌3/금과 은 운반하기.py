def solution(a, b, g, s, w, t):
    start = 0
    end = 10 ** 9 * 10 ** 5 * 4 - 10 ** 5
    answer = end

    while start <= end:
        mid = (start + end) // 2

        max_g, min_g, max_s, min_s = 0, 0, 0, 0
        for i in range(len(t)):
            cnt = (mid - t[i]) // (2 * t[i]) + 1

            # 금을 최우선으로 담을 때의 금과 은의 양
            max_g += g[i] if g[i] <= cnt * w[i] else cnt * w[i]
            min_s += min(s[i], cnt * w[i] - g[i]) if g[i] <= cnt * w[i] else 0

            # 은을 최우선으로 담을 때의 금과 은의 양
            max_s += s[i] if s[i] <= cnt * w[i] else cnt * w[i]
            min_g += min(g[i], cnt * w[i] - s[i]) if s[i] <= cnt * w[i] else 0

        if max_g >= a and max_s >= b and max_g + min_s >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    return answer


print(solution(10, 10, [100], [100], [7], [10]))  # 50