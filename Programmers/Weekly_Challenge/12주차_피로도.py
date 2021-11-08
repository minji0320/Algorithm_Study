from itertools import permutations


def solution(k, dungeons):
    answer = 0
    orders = permutations(dungeons)
    for order in orders:
        cnt = 0
        now = k
        for requirement, consumption in order:
            if now >= requirement:
                now -= consumption
                cnt += 1

        if answer < cnt:
            answer = cnt

    return answer
