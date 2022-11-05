def solution(n):
    answer = 0
    while(1):
        answer += n % 10
        n/10
    return answer