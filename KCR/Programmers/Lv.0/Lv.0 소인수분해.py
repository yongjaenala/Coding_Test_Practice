def solution(n):
    answer = []

    # 소수 저장
    prime = []
    for i in range(2, 10000) :
        for j in range(2, i) :
            if i%j == 0 :
                break
            if j == i-1 :
                prime.append(i)
    prime.insert(0, 2) # 2도 소수니까 추가

    for i in range(2, n+1) :
        if (n%i == 0) & (i in prime) :
            answer.append(i)
    return answer