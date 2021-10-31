import sys

# 학생 위치 배치하기
def assign(num):
    max_match = -1
    temp = []
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for x in range(N):
        for y in range(N):
            if classroom[x][y] == "0":
                match = len(favorite[num] & neighbors[(x, y)])
                if match > max_match:
                    max_match = match
                    temp = []
                if match == max_match:
                    empty = 4 - len(neighbors[(x, y)])
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 > nx or nx >= N or 0 > ny or ny >= N:
                            empty -= 1
                    temp.append(((x, y), empty))
    temp.sort(key=lambda k: (-k[1], k[0]))
    x, y = temp[0][0][0], temp[0][0][1]
    classroom[x][y] = num

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            continue
        neighbors[(nx, ny)].add(num)

# 만족도 구하기
def calc():
    total = 0
    point = [0, 1, 10, 100, 1000]
    for i in range(N):
        for j in range(N):
            match = len(favorite[classroom[i][j]] & neighbors[(i, j)])
            total += point[match]
    return total


N = int(sys.stdin.readline())

# 이웃, 교실 정보 초기화
neighbors = {}
classroom = []
for i in range(N):
    classroom.append([])
    for j in range(N):
        neighbors[(i, j)] = set()
        classroom[i].append("0")

# 선호 학생 저장, 학생 배치
favorite = {}
for i in range(N * N):
    temp = sys.stdin.readline().split()
    favorite[temp[0]] = set(temp[1:])
    assign(temp[0])

# 학생의 만족도의 총합 구하기
print(calc())
