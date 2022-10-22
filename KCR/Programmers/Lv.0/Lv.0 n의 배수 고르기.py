def solution(n, numlist):
    answer = []
    for i in numlist :
        if i%n == 0 :  # 나머지가 0이면 n의 배수
            answer.append(i)
    return answer