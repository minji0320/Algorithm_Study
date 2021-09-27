# https://programmers.co.kr/learn/courses/30/lessons/86048?language=python3

def solution(enter, leave):
    n = len(enter)
    meet = {}
    for i in range(n):
        meet[i + 1] = set()

    room = []
    e_idx = 0
    l_idx = 0
    cnt = 0
    is_enter = False
    while l_idx != n:
        if e_idx != n and leave[l_idx] not in room:
            room.append(enter[e_idx])
            cnt += 1
            is_enter = True
            for i in range(cnt):
                meet[room[i]].add(enter[e_idx])
                meet[enter[e_idx]].add(room[i])

        if (e_idx != n and enter[e_idx] == leave[l_idx]) or leave[l_idx] in room:
            room.remove(leave[l_idx])
            cnt -= 1
            l_idx += 1

        if is_enter:
            e_idx += 1

        is_enter = False

    answer = []
    for i in range(n):
        answer.append(len(meet[i + 1]) - 1)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.05ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.26ms, 10.3MB)
# 테스트 7 〉	통과 (0.13ms, 10.3MB)
# 테스트 8 〉	통과 (0.38ms, 10.4MB)
# 테스트 9 〉	통과 (0.61ms, 10.4MB)
# 테스트 10 〉	통과 (7.36ms, 12MB)
# 테스트 11 〉	통과 (27.69ms, 22.3MB)
# 테스트 12 〉	통과 (46.15ms, 26.7MB)
# 테스트 13 〉	통과 (0.01ms, 10.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.02ms, 10.3MB)
# 테스트 17 〉	통과 (0.01ms, 10.3MB)
# 테스트 18 〉	통과 (0.03ms, 10.3MB)
# 테스트 19 〉	통과 (0.03ms, 10.3MB)
# 테스트 20 〉	통과 (0.02ms, 10.3MB)
# 테스트 21 〉	통과 (1.26ms, 10.6MB)
# 테스트 22 〉	통과 (0.75ms, 10.5MB)
# 테스트 23 〉	통과 (0.21ms, 10.4MB)
# 테스트 24 〉	통과 (39.75ms, 25.2MB)
# 테스트 25 〉	통과 (20.89ms, 17.4MB)
# 테스트 26 〉	통과 (149.46ms, 41.1MB)
# 테스트 27 〉	통과 (96.18ms, 38.2MB)
# 테스트 28 〉	통과 (0.02ms, 10.3MB)
# 테스트 29 〉	통과 (0.05ms, 10.3MB)
# 테스트 30 〉	통과 (0.67ms, 10.4MB)
# 테스트 31 〉	통과 (3.72ms, 11.1MB)
# 테스트 32 〉	통과 (16.48ms, 15.4MB)
# 테스트 33 〉	통과 (65.06ms, 30.8MB)
# 테스트 34 〉	통과 (68.78ms, 32.4MB)
# 테스트 35 〉	통과 (0.04ms, 10.3MB)
# 테스트 36 〉	통과 (0.15ms, 10.3MB)
# 테스트 37 〉	통과 (0.01ms, 10.3MB)
