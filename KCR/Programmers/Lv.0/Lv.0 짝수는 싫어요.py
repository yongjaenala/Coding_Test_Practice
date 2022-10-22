def solution(n):
    answer = []
    for i in range(n+1) : # 1부터 n까지를 확인해야 하기 때문에
        if i%2 != 0 :
            answer.append(i)
    return answer