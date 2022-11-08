def solution(left, right):
    answer = 0
    for i in range(left, right+1) :
        cnt = 0
        for j in range(i, 0, -1) :
            if i%j == 0 :
                cnt += 1
        if cnt%2 == 0 :
            answer += i
        else :
            answer -= i
    return answer

# 제곱수의 약수는 홀수개...?
# 즉
# if int(i**0.5) == i**0.5 ...
# for문을 하나만 돌려도 된다..!
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer