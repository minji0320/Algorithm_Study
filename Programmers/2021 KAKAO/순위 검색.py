def solution(info, query):
    n = len(query)
    answer = [0 for _ in range(n)]
    applicants = []
    for i in info:
        applicants.append(i.split(" "))

    for i, q in enumerate(query):
        q_lang, q_part, q_career, q_food_score = q.split(" and ")
        q_food, q_score = q_food_score.split(" ")
        for applicant in applicants:
            if ((q_lang == "-" or q_lang == applicant[0])
                    and (q_part == "-" or q_part == applicant[1])
                    and (q_career == "-" or q_career == applicant[2])
                    and (q_food == "-" or q_food == applicant[3])
                    and int(q_score) <= int(applicant[4])):
                answer[i] += 1

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.06ms, 10.4MB)
# 테스트 2 〉	통과 (0.08ms, 10.4MB)
# 테스트 3 〉	통과 (0.55ms, 10.4MB)
# 테스트 4 〉	통과 (5.48ms, 10.5MB)
# 테스트 5 〉	통과 (21.95ms, 10.6MB)
# 테스트 6 〉	통과 (37.63ms, 10.5MB)
# 테스트 7 〉	통과 (27.71ms, 10.5MB)
# 테스트 8 〉	통과 (78.05ms, 12.8MB)
# 테스트 9 〉	통과 (84.97ms, 12.8MB)
# 테스트 10 〉	통과 (84.07ms, 12.9MB)
# 테스트 11 〉	통과 (13.63ms, 10.5MB)
# 테스트 12 〉	통과 (43.23ms, 10.5MB)
# 테스트 13 〉	통과 (18.21ms, 10.5MB)
# 테스트 14 〉	통과 (73.17ms, 11.4MB)
# 테스트 15 〉	통과 (86.62ms, 11.5MB)
# 테스트 16 〉	통과 (18.66ms, 10.5MB)
# 테스트 17 〉	통과 (38.12ms, 10.4MB)
# 테스트 18 〉	통과 (78.47ms, 11.5MB)
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)

def solution(info, query):
    # applicants : 지원자 정보를 key 값, 지원자들의 점수를 value 값으로 갖도록 저장
    all_options = [["cpp", "java", "python"],
                   ["backend", "frontend"],
                   ["junior", "senior"],
                   ["chicken", "pizza"]]
    n = len(query)
    answer = [0 for _ in range(n)]
    applicants = {}
    for i in info:
        temp = ""
        now_info = i.split(" ")
        for idx, a in enumerate(now_info):
            if idx == 4:
                break
            temp += str(all_options[idx].index(a))
        if temp not in applicants:
            applicants[temp] = []
        applicants[temp].append(int(now_info[4]))

    # info와 비교 가능한 형태로 쿼리를 수정하여 해당하는 지원자 수 구하기
    for i, q in enumerate(query):
        # "-"가 포함된 쿼리인 경우, 지원자 정보와 비교 가능하도록 수정
        now = q.split(" and ")
        now += now[3].split(" ")
        now.remove(now[3])
        result = [""]
        for j in range(4):
            if now[j] == "-":
                temp = result
                result = []
                for t in temp:
                    for k in range(len(all_options[j])):
                        result.append(t + str(k))
            else:
                for k in range(len(result)):
                    result[k] += str(all_options[j].index(now[j]))

        # 쿼리에 해당하는 지원자 수 구하기
        for r in result:
            if r in applicants:
                for score in applicants[r]:
                    if score >= int(now[4]):
                        answer[i] += 1

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.24ms, 10.5MB)
# 테스트 2 〉	통과 (0.13ms, 10.4MB)
# 테스트 3 〉	통과 (0.88ms, 10.5MB)
# 테스트 4 〉	통과 (10.96ms, 10.5MB)
# 테스트 5 〉	통과 (16.78ms, 10.5MB)
# 테스트 6 〉	통과 (19.49ms, 10.5MB)
# 테스트 7 〉	통과 (16.16ms, 10.6MB)
# 테스트 8 〉	통과 (39.09ms, 10.6MB)
# 테스트 9 〉	통과 (39.73ms, 10.7MB)
# 테스트 10 〉	통과 (24.76ms, 10.7MB)
# 테스트 11 〉	통과 (15.85ms, 10.5MB)
# 테스트 12 〉	통과 (10.12ms, 10.4MB)
# 테스트 13 〉	통과 (14.49ms, 10.6MB)
# 테스트 14 〉	통과 (18.48ms, 10.6MB)
# 테스트 15 〉	통과 (18.73ms, 10.6MB)
# 테스트 16 〉	통과 (8.76ms, 10.5MB)
# 테스트 17 〉	통과 (10.85ms, 10.5MB)
# 테스트 18 〉	통과 (17.55ms, 10.6MB)
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)

def solution(info, query):
    # applicants : 지원자 정보를 key 값, 지원자들의 점수를 value 값으로 갖도록 저장
    all_options = [["cpp", "java", "python"],
                   ["backend", "frontend"],
                   ["junior", "senior"],
                   ["chicken", "pizza"]]
    n = len(query)
    answer = [0 for _ in range(n)]
    applicants = {}
    for i in info:
        temp = ""
        now_info = i.split(" ")
        for idx, a in enumerate(now_info):
            if idx == 4:
                break
            temp += str(all_options[idx].index(a))
        if temp not in applicants:
            applicants[temp] = []
        applicants[temp].append(int(now_info[4]))

    for a in applicants:
        applicants[a].sort()

    # info와 비교 가능한 형태로 쿼리를 수정하여 해당하는 지원자 수 구하기
    for i, q in enumerate(query):
        # "-"가 포함된 쿼리인 경우, 지원자 정보와 비교 가능하도록 수정
        now = q.split(" and ")
        now += now[3].split(" ")
        now.remove(now[3])
        result = [""]
        for j in range(4):
            if now[j] == "-":
                temp = result
                result = []
                for t in temp:
                    for k in range(len(all_options[j])):
                        result.append(t + str(k))
            else:
                for k in range(len(result)):
                    result[k] += str(all_options[j].index(now[j]))

        # 쿼리에 해당하는 지원자 수 구하기
        for r in result:
            if r in applicants:
                left, right = 0, len(applicants[r])
                while left < right:
                    mid = (left + right) // 2
                    if applicants[r][mid] >= int(now[4]):
                        right = mid
                    else:
                        left = mid + 1
                answer[i] += (len(applicants[r]) - left)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.13ms, 10.4MB)
# 테스트 2 〉	통과 (0.12ms, 10.5MB)
# 테스트 3 〉	통과 (0.67ms, 10.5MB)
# 테스트 4 〉	통과 (6.13ms, 10.5MB)
# 테스트 5 〉	통과 (8.35ms, 10.6MB)
# 테스트 6 〉	통과 (5.65ms, 10.5MB)
# 테스트 7 〉	통과 (13.86ms, 10.8MB)
# 테스트 8 〉	통과 (10.47ms, 10.5MB)
# 테스트 9 〉	통과 (13.48ms, 10.8MB)
# 테스트 10 〉	통과 (10.47ms, 11.1MB)
# 테스트 11 〉	통과 (8.09ms, 10.5MB)
# 테스트 12 〉	통과 (5.97ms, 10.5MB)
# 테스트 13 〉	통과 (14.08ms, 10.7MB)
# 테스트 14 〉	통과 (7.02ms, 10.7MB)
# 테스트 15 〉	통과 (7.39ms, 10.8MB)
# 테스트 16 〉	통과 (7.78ms, 10.5MB)
# 테스트 17 〉	통과 (6.10ms, 10.5MB)
# 테스트 18 〉	통과 (6.55ms, 10.7MB)
# 효율성  테스트
# 테스트 1 〉	통과 (1703.63ms, 35.6MB)
# 테스트 2 〉	통과 (1791.03ms, 36MB)
# 테스트 3 〉	통과 (8660.51ms, 35.6MB)
# 테스트 4 〉	통과 (8464.35ms, 35.9MB)

def solution(info, query):
    # applicants :  key - (지원자 정보), value - [지원자들의 점수]
    n = len(query)
    applicants = {}
    for i in info:
        temp = ""
        now_info = i.split(" ")
        for a in [now_info[0], "-"]:
            for b in [now_info[1], "-"]:
                for c in [now_info[2], "-"]:
                    for d in [now_info[3], "-"]:
                        if (a, b, c, d) not in applicants:
                            applicants[(a, b, c, d)] = []
                        applicants[(a, b, c, d)].append(int(now_info[4]))

    for a in applicants:
        applicants[a].sort()

    # 쿼리에 해당하는 지원자 수 구하기
    answer = [0 for _ in range(n)]
    for i, q in enumerate(query):
        now_query = q.replace("and ", "")
        f_idx = now_query.rfind(" ")
        now_query, score = tuple(now_query[:f_idx].split(" ")), int(now_query[f_idx + 1:])

        # 이분탐색 활용하여 쿼리에 해당하는 지원자 수 구하기
        if now_query in applicants:
            left, right = 0, len(applicants[now_query])
            while left < right:
                mid = (left + right) // 2
                if applicants[now_query][mid] >= score:
                    right = mid
                else:
                    left = mid + 1
            answer[i] = (len(applicants[now_query]) - left)

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.39ms, 10.4MB)
# 테스트 2 〉	통과 (0.27ms, 10.5MB)
# 테스트 3 〉	통과 (0.38ms, 10.5MB)
# 테스트 4 〉	통과 (3.20ms, 10.5MB)
# 테스트 5 〉	통과 (3.25ms, 10.5MB)
# 테스트 6 〉	통과 (6.23ms, 10.6MB)
# 테스트 7 〉	통과 (4.88ms, 10.8MB)
# 테스트 8 〉	통과 (48.66ms, 11.4MB)
# 테스트 9 〉	통과 (64.40ms, 13.2MB)
# 테스트 10 〉	통과 (60.43ms, 13.8MB)
# 테스트 11 〉	통과 (5.83ms, 10.6MB)
# 테스트 12 〉	통과 (6.26ms, 10.7MB)
# 테스트 13 〉	통과 (7.95ms, 10.8MB)
# 테스트 14 〉	통과 (24.44ms, 12.2MB)
# 테스트 15 〉	통과 (27.08ms, 12.3MB)
# 테스트 16 〉	통과 (3.23ms, 10.6MB)
# 테스트 17 〉	통과 (6.14ms, 10.7MB)
# 테스트 18 〉	통과 (24.06ms, 12.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (1029.44ms, 63.3MB)
# 테스트 2 〉	통과 (1034.98ms, 63.7MB)
# 테스트 3 〉	통과 (999.51ms, 63.4MB)
# 테스트 4 〉	통과 (904.92ms, 63.9MB)