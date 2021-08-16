# https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3

import heapq


def solution(jobs):
    # 작업 요청 시간이 빠른 순, 소요시간이 적은 순으로 정렬하여 (소요 시간, 요청 시간)으로 저장
    sorted_jobs = sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0]))

    n = len(jobs)
    time = sorted_jobs[0][1]
    total_time = 0
    idx = 0
    heap = []

    while True:
        # 모든 디스크 수행 완료인 경우
        if idx == n and len(heap) == 0:
            return total_time // n

        # 현재 시간에 수행 가능한 디스크가 있는 경우 힙에 넣기
        while idx < n and sorted_jobs[idx][1] <= time:
            heapq.heappush(heap, sorted_jobs[idx])
            idx += 1

        # 가장 소요시간이 짧은 작업 수행
        if len(heap) > 0:
            temp = heapq.heappop(heap)
            total_time += temp[0] + time - temp[1]
            time += temp[0]
        else:
            time = sorted_jobs[idx][1]

### 정확성  테스트
# 테스트 1 〉	통과 (0.66ms, 10.4MB)
# 테스트 2 〉	통과 (0.95ms, 10.3MB)
# 테스트 3 〉	통과 (0.67ms, 10.3MB)
# 테스트 4 〉	통과 (0.51ms, 10.3MB)
# 테스트 5 〉	통과 (0.64ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.41ms, 10.3MB)
# 테스트 8 〉	통과 (0.31ms, 10.2MB)
# 테스트 9 〉	통과 (0.14ms, 10.3MB)
# 테스트 10 〉	통과 (1.09ms, 10.4MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.02ms, 10.3MB)
# 테스트 13 〉	통과 (0.02ms, 10.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.4MB)
# 테스트 15 〉	통과 (0.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (0.01ms, 10.3MB)
# 테스트 18 〉	통과 (0.01ms, 10.3MB)
# 테스트 19 〉	통과 (0.01ms, 10.3MB)
# 테스트 20 〉	통과 (0.01ms, 10.3MB)