def solution(absolutes, signs):
    answer = 0
    
    for i, abs_num in enumerate(absolutes):
        if signs[i]:
            answer += abs_num
        else:
            answer -= abs_num

    return answer