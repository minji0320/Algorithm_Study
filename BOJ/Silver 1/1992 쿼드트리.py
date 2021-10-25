import sys

def quad_tree(x, y, n):
    global arr
    first = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != first:
                result = "("
                result += quad_tree(x, y, n // 2)
                result += quad_tree(x, y + n // 2, n // 2)
                result += quad_tree(x + n // 2, y, n // 2)
                result += quad_tree(x + n // 2, y + n // 2, n // 2)
                result += ")"
                return result
    return first

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
print(quad_tree(0, 0, N))
