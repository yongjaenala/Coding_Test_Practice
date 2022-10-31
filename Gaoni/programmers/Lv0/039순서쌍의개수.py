def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if n % i == 0:
            answer += 1
    return answer
#     for i in range(1, int((n**(1/2)))):
#         for j in range(int((n**(1/2))),n+1):
#             if i*j ==n:
#                 answer += 1
#             else:
#                 continue

#     if n%(n**(1/2))==0:
#         return answer*2-1
#     else:
#         return answer*2


