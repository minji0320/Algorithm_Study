### 문제 설명
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

### 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.

### 입출력 예
# participant	completion	return
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"

### 입출력 예 설명
## 예제 #1
# "leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
## 예제 #2
# "vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
## 예제 #3
# "mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.


def solution(participant, completion):
    dic = {}
    for comp in completion:
        if comp not in dic:
            dic[comp] = 0
        dic[comp] += 1
    for part in participant:
        if part not in dic or dic[part] == 0:
            return part
        dic[part] -= 1

### 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.12ms, 10.2MB)
# 테스트 4 〉	통과 (0.30ms, 10.3MB)
# 테스트 5 〉	통과 (0.26ms, 10.5MB)

### 효율성  테스트
# 테스트 1 〉	통과 (16.20ms, 21.8MB)
# 테스트 2 〉	통과 (28.91ms, 25.2MB)
# 테스트 3 〉	통과 (33.32ms, 27.6MB)
# 테스트 4 〉	통과 (29.59ms, 34MB)
# 테스트 5 〉	통과 (58.58ms, 33.9MB)


# 다른 사람의 풀이
def solution2(participant, completion):
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

### 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.27ms, 10.3MB)
# 테스트 4 〉	통과 (0.81ms, 10.4MB)
# 테스트 5 〉	통과 (0.73ms, 10.5MB)

### 효율성  테스트
# 테스트 1 〉	통과 (22.66ms, 23.8MB)
# 테스트 2 〉	통과 (36.69ms, 28.4MB)
# 테스트 3 〉	통과 (45.68ms, 31.4MB)
# 테스트 4 〉	통과 (54.14ms, 37.8MB)
# 테스트 5 〉	통과 (54.66ms, 37.7MB)