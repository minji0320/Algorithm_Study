### 문제 설명
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다.
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
# 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다.
# 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

# 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다.
# 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

# 경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
# 0	        []	            []	            [7,4,5,6]
# 1~2	    []	            [7]	            [4,5,6]
# 3	        [7]	            [4]	            [5,6]
# 4	        [7]	            [4,5]	        [6]
# 5	        [7,4]	        [5]	            [6]
# 6~7	    [7,4,5]	        [6]	            []
# 8	        [7,4,5,6]	    []	            []
# 따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

# solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다.
# 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

### 제한 조건
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.

### 입출력 예
# bridge_length	weight	truck_weights	                    return
# 2	            10	    [7,4,5,6]	                        8
# 100	        100	    [10]	                            101
# 100	        100	    [10,10,10,10,10,10,10,10,10,10]	    110

def solution(bridge_length, weight, truck_weights):
    time = 0
    start_idx = 0
    end_idx = 0
    n = len(truck_weights)
    remaining_weights = weight
    remaining_distance = [bridge_length] * n

    while True:
        time += 1

        # 마지막 트럭이 다리에 오른 경우
        if end_idx == n:
            return time + remaining_distance[end_idx - 1]

        # 이번 순서의 트럭이 다리에 올라갈 수 있는 경우
        if remaining_weights - truck_weights[end_idx] >= 0:
            remaining_weights -= truck_weights[end_idx]
            end_idx += 1

        # 다리에 올라간 트럭들 이동
        for i in range(start_idx, end_idx):
            remaining_distance[i] -= 1
            if remaining_distance[i] == 0:
                remaining_weights += truck_weights[start_idx]
                start_idx += 1

### 정확성  테스트 -> 너무 느림!
# 테스트 1 〉	통과 (0.60ms, 10.2MB)
# 테스트 2 〉	통과 (12.54ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (56.16ms, 10.3MB)
# 테스트 5 〉	통과 (457.22ms, 10.3MB)
# 테스트 6 〉	통과 (183.67ms, 10.2MB)
# 테스트 7 〉	통과 (0.57ms, 10.3MB)
# 테스트 8 〉	통과 (0.16ms, 10.3MB)
# 테스트 9 〉	통과 (4.66ms, 10.3MB)
# 테스트 10 〉	통과 (0.17ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.44ms, 10.2MB)
# 테스트 13 〉	통과 (1.14ms, 10.3MB)
# 테스트 14 〉	통과 (0.00ms, 10.3MB)


def solution2(bridge_length, weight, truck_weights):
    time = 0
    start_idx = 0
    end_idx = 0
    travel_distance = 0
    n = len(truck_weights)
    remaining_weights = weight
    remaining_distance = [bridge_length] * n

    while True:
        time += 1

        # 마지막 트럭이 다리에 오른 경우
        if end_idx == n:
            return time + remaining_distance[end_idx - 1]

        # 이번 순서의 트럭이 다리에 올라갈 수 있는 경우
        if remaining_weights - truck_weights[end_idx] >= 0:
            remaining_weights -= truck_weights[end_idx]
            end_idx += 1
            travel_distance = 1
        else:
            travel_distance = remaining_distance[start_idx]


        # 다리에 올라간 트럭들 이동
        time += travel_distance - 1
        for i in range(start_idx, end_idx):
            remaining_distance[i] -= travel_distance
            if remaining_distance[i] == 0:
                remaining_weights += truck_weights[start_idx]
                start_idx += 1

### 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.78ms, 10.3MB)
# 테스트 5 〉	통과 (1.33ms, 10.2MB)
# 테스트 6 〉	통과 (1.22ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.3MB)
# 테스트 9 〉	통과 (0.58ms, 10.3MB)
# 테스트 10 〉	통과 (0.02ms, 10.4MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.06ms, 10.3MB)
# 테스트 13 〉	통과 (0.07ms, 10.3MB)
# 테스트 14 〉	통과 (0.00ms, 10.2MB)