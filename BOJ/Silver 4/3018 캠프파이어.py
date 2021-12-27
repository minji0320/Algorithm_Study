import sys
import copy

N = int(sys.stdin.readline())
E = int(sys.stdin.readline())

songs = [set() for _ in range(N + 1)]
idx = 0
for i in range(E):
    participants = list(map(int, sys.stdin.readline().split()))
    # 선영이가 참가한 경우, 새로운 노래 추가
    if 1 in participants:
        for participant in participants[1:]:
            songs[participant].add(idx)
    # 참가하지 않은 경우, 각자 아는 노래 공유
    else:
        now_songs = set()
        for participant in participants[1:]:
            now_songs |= songs[participant]
        for participant in participants[1:]:
            songs[participant] = copy.deepcopy(now_songs)
    idx += 1

answer = [1]
target_cnt = len(songs[1])
for i in range(2, N + 1):
    if len(songs[i]) == target_cnt:
        answer.append(i)

answer.sort()
for a in answer:
    print(a)
