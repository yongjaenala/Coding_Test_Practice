# 빈병a개 -> 코라b병
# 콜라n병 -> 최대 몇병?


def solution(a,b,n):
    answer = 0
    while a <= n:
        answer += n//a
        n = n//a + n%a

    return answer


print(solution(2,1,20))
print(solution(3,1,20))