def solution(grid):
    def move(x, y, d):
        cnt = 0
        while (x, y, d) not in routes:
            routes[(x, y, d)] = 1
            x += dirs[d][0]
            y += dirs[d][1]

            if 0 > x:
                x = n - 1
            elif x >= n:
                x = 0
            elif 0 > y:
                y = m - 1
            elif y >= m:
                y = 0

            if grid[x][y] == "L":
                d = (d + 3) % 4
            elif grid[x][y] == "R":
                d = (d + 1) % 4

            cnt += 1

        return cnt

    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    n, m = len(grid), len(grid[0])

    routes = {}
    answer = []
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if (i, j, k) not in routes:
                    routes_len = move(i, j, k)
                    answer.append(routes_len)

    answer.sort()
    return answer
