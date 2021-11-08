def solution(n, k, cmd):
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    result = ["O" for _ in range(n)]
    stack = []
    for c in cmd:
        if c[0] == "U":
            for _ in range(int(c[2:])):
                k = linked_list[k][0]
        elif c[0] == "D":
            for _ in range(int(c[2:])):
                k = linked_list[k][1]
        elif c[0] == "C":
            prev, next = linked_list[k]
            stack.append([prev, k, next])
            result[k] = "X"
            if next == n:
                k = prev
                linked_list[prev][1] = next
            else:
                k = next
                if prev == -1:
                    linked_list[next][0] = prev
                else:
                    linked_list[prev][1] = next
                    linked_list[next][0] = prev
        elif c[0] == "Z":
            prev, now, next = stack.pop()
            result[now] = "O"
            if next == n:
                linked_list[prev][1] = now
            else:
                if prev == -1:
                    linked_list[next][0] = now
                else:
                    linked_list[prev][1] = now
                    linked_list[next][0] = now

    return "".join(result)