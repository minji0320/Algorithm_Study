def time_to_seconds(time):
    hours, minutes, seconds = time.split(":")
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)

def seconds_to_time(seconds):
    hours = str(seconds // 3600)
    if len(hours) == 1:
        hours = '0' + hours
    seconds %= 3600

    minutes = str(seconds // 60)
    if len(minutes) == 1:
        minutes = '0' + minutes
    seconds %= 60

    seconds = str(seconds)
    if len(seconds) == 1:
        seconds = '0' + seconds

    return hours + ':' + minutes + ':' + seconds

def solution(play_time, adv_time, logs):
    # 플레이 시간 별 시청자 수 구하기
    play_seconds = time_to_seconds(play_time)
    start_end = [log.split("-") for log in logs]
    viewers = [0] * (play_seconds + 1)
    for start, end in start_end:
        viewers[time_to_seconds(start)] += 1
        viewers[time_to_seconds(end)] -= 1
    for i in range(1, play_seconds + 1):
        viewers[i] = viewers[i - 1] + viewers[i]

    # 누적 시청자 수 구하기
    for i in range(1, play_seconds + 1):
        viewers[i] = viewers[i - 1] + viewers[i]

    # 누적 시청자 수가 가장 많은 구간 구하기
    adv_seconds = time_to_seconds(adv_time)
    max_viewers = viewers[adv_seconds - 1]
    max_seconds = 0
    for i in range(adv_seconds, play_seconds):
        if max_viewers < viewers[i] - viewers[i - adv_seconds]:
            max_viewers = viewers[i] - viewers[i - adv_seconds]
            max_seconds = i - adv_seconds + 1

    return seconds_to_time(max_seconds)

# 정확성  테스트
# 테스트 1 〉	통과 (1.63ms, 10.7MB)
# 테스트 2 〉	통과 (7.75ms, 12.2MB)
# 테스트 3 〉	통과 (17.97ms, 13.9MB)
# 테스트 4 〉	통과 (187.06ms, 41.6MB)
# 테스트 5 〉	통과 (302.55ms, 61.4MB)
# 테스트 6 〉	통과 (104.97ms, 21.7MB)
# 테스트 7 〉	통과 (518.08ms, 98.9MB)
# 테스트 8 〉	통과 (501.63ms, 104MB)
# 테스트 9 〉	통과 (779.49ms, 140MB)
# 테스트 10 〉	통과 (780.64ms, 141MB)
# 테스트 11 〉	통과 (852.86ms, 138MB)
# 테스트 12 〉	통과 (833.30ms, 136MB)
# 테스트 13 〉	통과 (846.27ms, 141MB)
# 테스트 14 〉	통과 (644.75ms, 124MB)
# 테스트 15 〉	통과 (42.77ms, 15MB)
# 테스트 16 〉	통과 (619.23ms, 123MB)
# 테스트 17 〉	통과 (768.25ms, 141MB)
# 테스트 18 〉	통과 (733.04ms, 128MB)
# 테스트 19 〉	통과 (1.52ms, 10.5MB)
# 테스트 20 〉	통과 (1.40ms, 10.5MB)
# 테스트 21 〉	통과 (171.58ms, 47.5MB)
# 테스트 22 〉	통과 (183.58ms, 47.4MB)
# 테스트 23 〉	통과 (756.91ms, 133MB)
# 테스트 24 〉	통과 (688.26ms, 125MB)
# 테스트 25 〉	통과 (79.26ms, 19.7MB)
# 테스트 26 〉	통과 (52.97ms, 15MB)
# 테스트 27 〉	통과 (59.14ms, 17.3MB)
# 테스트 28 〉	통과 (59.20ms, 16.8MB)
# 테스트 29 〉	통과 (55.32ms, 16.9MB)
# 테스트 30 〉	통과 (40.45ms, 14.3MB)
# 테스트 31 〉	통과 (42.13ms, 14.9MB)
