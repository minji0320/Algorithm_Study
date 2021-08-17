# https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq


def solution(operations):
    min_heap = []
    cnt = 0
    for operation in operations:
        temp = operation.split(' ')
        eng = temp[0]
        num = int(temp[1])
        if eng == 'I':
            # 숫자 삽입
            heapq.heappush(min_heap, num)
            cnt += 1
        elif num == 1 and cnt > 0:
            # 최댓값 삭제
            min_heap.remove(max(min_heap))
            cnt -= 1
        elif num == -1 and cnt > 0:
            # 최솟값 삭제
            heapq.heappop(min_heap)
            cnt -= 1

    answer = []
    if cnt == 0:
        answer = [0, 0]
    else:
        answer.append(max(min_heap))
        answer.append(heapq.heappop(min_heap))

    return answer

### 정확성  테스트
# 테스트 1 〉	통과 (0.03ms, 10.5MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.02ms, 10.4MB)
# 테스트 5 〉	통과 (0.02ms, 10.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.5MB)