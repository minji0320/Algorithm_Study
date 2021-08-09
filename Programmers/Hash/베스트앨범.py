### 문제 설명
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
# 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

### 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.

### 입출력 예
# genres	                                        plays	                    return
# ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

### 입출력 예 설명
# classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.
# 고유 번호 3: 800회 재생
# 고유 번호 0: 500회 재생
# 고유 번호 2: 150회 재생
# pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.
# 고유 번호 4: 2,500회 재생
# 고유 번호 1: 600회 재생
# 따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

def solution(genres, plays):
    total_count = {}
    genre_items = {}

    n = len(genres)
    for i in range(n):
        # 장르별 재생 총합 구하기
        if genres[i] not in total_count:
            total_count[genres[i]] = 0
        total_count[genres[i]] += plays[i]

        # 장르별 노래(인덱스, 재생 횟수) 저장
        if genres[i] not in genre_items:
            genre_items[genres[i]] = []
        genre_items[genres[i]].append((i, plays[i]))

    # 장르별 재생 총합이 높은 순으로 정렬
    total_count = sorted(total_count.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for genre in total_count:
        # 각 장르별로 재생 횟수가 높은 노래 순으로 정렬
        sorted_genre_items = sorted(genre_items[genre[0]], key=lambda x: x[1], reverse=True)
        temp_cnt = 0
        for item in sorted_genre_items:
            # 최대 2곡 추가
            if temp_cnt == 2:
                break

            answer.append(item[0])
            temp_cnt += 1

    return answer


### 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.06ms, 10.2MB)
# 테스트 6 〉	통과 (0.09ms, 10.3MB)
# 테스트 7 〉	통과 (0.05ms, 10.2MB)
# 테스트 8 〉	통과 (0.05ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.11ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.2MB)
# 테스트 12 〉	통과 (0.05ms, 10.3MB)
# 테스트 13 〉	통과 (0.10ms, 10.2MB)
# 테스트 14 〉	통과 (0.11ms, 10.2MB)
# 테스트 15 〉	통과 (0.02ms, 10.2MB)