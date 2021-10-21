def solution(s):
    answer = ""
    n = len(s)
    num_dict = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
                '6': '6', '7': '7', '8': '8', '9': '9',
                'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    start = 0
    for i in range(1, n + 1):
        if s[start:i] in num_dict:
            answer += num_dict[s[start:i]]
            start = i
    return int(answer)