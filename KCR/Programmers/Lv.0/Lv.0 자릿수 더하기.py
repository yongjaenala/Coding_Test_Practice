def solution(n):
    answer = 0
    for i in str(n) :  # 각 자리의 수를 하나씩 가져오기 위함
        answer += int(i)
    return answer