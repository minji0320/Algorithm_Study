N = int(input())
result = [0, 1]
for i in range(1, N):
    result.append(result[i] + result[i-1])

print(result[-1])
