### 문제 설명
# 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
# 예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면
# 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

# 종류	이름
# 얼굴	동그란 안경, 검정 선글라스
# 상의	파란색 티셔츠
# 하의	청바지
# 겉옷	긴 코트

# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때
# 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

### 제한사항
# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
# 같은 이름을 가진 의상은 존재하지 않습니다.
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
# 스파이는 하루에 최소 한 개의 의상은 입습니다.

### 입출력 예
# clothes	return
# [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	5
# [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	3

### 입출력 예 설명
## 예제 #1
# headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.
# 1. yellow_hat
# 2. blue_sunglasses
# 3. green_turban
# 4. yellow_hat + blue_sunglasses
# 5. green_turban + blue_sunglasses

# 예제 #2
## face에 해당하는 의상이 crow_mask, blue_sunglasses, smoky_makeup이므로 아래와 같이 3개의 조합이 가능합니다.
# 1. crow_mask
# 2. blue_sunglasses
# 3. smoky_makeup

def solution(clothes):
    type = {}
    for c, t in clothes:
        if t not in type:
            type[t] = 2
        else:
            type[t] += 1

    answer = 1
    for count in type.values():
        answer *= count
    return answer - 1

### 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.00ms, 10.2MB)
# 테스트 11 〉	통과 (0.00ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10MB)
# 테스트 16 〉	통과 (0.00ms, 10.1MB)
# 테스트 17 〉	통과 (0.01ms, 10.1MB)
# 테스트 18 〉	통과 (0.01ms, 10.1MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
# 테스트 21 〉	통과 (0.01ms, 10.1MB)
# 테스트 22 〉	통과 (0.00ms, 10.2MB)
# 테스트 23 〉	통과 (0.01ms, 10.2MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)
# 테스트 25 〉	통과 (0.01ms, 10.2MB)
# 테스트 26 〉	통과 (0.01ms, 10.1MB)
# 테스트 27 〉	통과 (0.01ms, 10.2MB)
# 테스트 28 〉	통과 (0.01ms, 10.2MB)
