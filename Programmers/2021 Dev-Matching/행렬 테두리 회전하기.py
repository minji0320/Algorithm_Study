def solution(rows, columns, queries):
    # 행렬 초기화
    answer = []
    arr = [[] for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            arr[i].append(num)
            num += 1

    # 테두리 회전
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        temp = arr[x1][y1]
        min_num = temp

        # 위로 이동
        for x in range(x1, x2):
            arr[x][y1] = arr[x + 1][y1]
            if min_num > arr[x][y1]:
                min_num = arr[x][y1]

        # 왼쪽으로 이동
        for y in range(y1, y2):
            arr[x2][y] = arr[x2][y + 1]
            if min_num > arr[x2][y]:
                min_num = arr[x2][y]

        # 아래로 이동
        for x in range(x2, x1, -1):
            arr[x][y2] = arr[x - 1][y2]
            if min_num > arr[x][y2]:
                min_num = arr[x][y2]

        # 오른쪽으로 이동
        for y in range(y2, y1, -1):
            arr[x1][y] = arr[x1][y - 1]
            if min_num > arr[x1][y]:
                min_num = arr[x1][y]

        arr[x1][y1 + 1] = temp
        answer.append(min_num)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (126.76ms, 11.8MB)
# 테스트 4 〉	통과 (67.57ms, 11.4MB)
# 테스트 5 〉	통과 (96.50ms, 11.4MB)
# 테스트 6 〉	통과 (126.53ms, 11.9MB)
# 테스트 7 〉	통과 (107.59ms, 12.2MB)
# 테스트 8 〉	통과 (130.85ms, 11.5MB)
# 테스트 9 〉	통과 (125.54ms, 12MB)
# 테스트 10 〉	통과 (73.46ms, 11.5MB)
# 테스트 11 〉	통과 (71.52ms, 11.5MB)