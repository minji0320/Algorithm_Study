def solution(dirs):
    direction = {"U": (-1, 0),
                 "D": (1, 0),
                 "R": (0, 1),
                 "L": (0, -1)}

    x, y = 0, 0
    routes = set()
    for i in dirs:
        dx, dy = direction[i][0], direction[i][1]
        nx, ny = x + dx, y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            routes.add((x, y, nx, ny))
            routes.add((nx, ny, x, y))
            x, y = nx, ny

    return len(routes) // 2
