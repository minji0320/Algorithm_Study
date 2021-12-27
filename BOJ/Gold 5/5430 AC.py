import sys
from collections import deque

read = sys.stdin.readline
T = int(read())
for _ in range(T):
    # 입력 받기
    p = read().strip()
    n = int(read())
    arr = read().strip()

    # 배열 deque에 저장
    q = deque()
    is_left = True
    if arr != "[]":
        q = deque(arr[1:-1].split(","))

    # 배열의 크기보다 D 함수가 더 많은 경우
    if p.count("D") > n:
        print("error")
        continue

    # 함수 수행
    for func in p:
        if func == "R":
            is_left = not is_left
        elif is_left:
            q.popleft()
        else:
            q.pop()

    q = list(q)
    if not is_left:
        q.reverse()
    print("[" + ",".join(q) + "]")
