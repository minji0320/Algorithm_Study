import sys
from itertools import combinations


def find_student():
    for teacher in teachers:
        for dx, dy in dirs:
            x, y = teacher[0], teacher[1]
            while True:
                nx, ny = x + dx, y + dy
                x, y = nx, ny
                if 0 <= nx < N and 0 <= ny < N:
                    if hallway[nx][ny] == "O":
                        break
                    if hallway[nx][ny] == "S":
                        return True
                else:
                    break
    return False


def solution():
    # 입력 받기, 선생님 위치 저장
    for i in range(N):
        hallway.append(sys.stdin.readline().split())
        for j in range(N):
            if hallway[i][j] == "T":
                teachers.append((i, j))

    # 장애물을 설치할 위치 후보 저장
    candidates = set()
    for teacher in teachers:
        for dx, dy in dirs:
            temp = []
            check = False
            x, y = teacher[0], teacher[1]
            while True:
                nx, ny = x + dx, y + dy
                x, y = nx, ny
                if 0 <= nx < N and 0 <= ny < N:
                    if hallway[nx][ny] == "S":
                        if len(temp) == 0:
                            return "NO"
                        else:
                            check = True
                            break
                    elif hallway[nx][ny] == "X":
                        temp.append((nx, ny))
                else:
                    break

            if check:
                candidates |= set(temp)

    if len(candidates) < 3:
        return "YES"

    comb = list(combinations(candidates, 3))
    for locs in comb:
        for x, y in locs:
            hallway[x][y] = "O"

        if not find_student():
            return "YES"

        for x, y in locs:
            hallway[x][y] = "X"

    return "NO"


N = int(sys.stdin.readline())
hallway = []
teachers = []
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
print(solution())
