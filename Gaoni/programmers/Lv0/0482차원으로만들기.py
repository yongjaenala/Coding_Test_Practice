def solution(num_list, n):
    answer = []

    # nl_len = len(num_list)
    #     for i in range(nl_len+1):
    #         for j in range(n+1):
    #             answer[i//n+1,j]=num_list[i]
    # for idx,i in enumerate(num_list):
    #     answer[(idx)//n, ]
    an = []

    for i in num_list:
        an.append(i)
        if len(an) == n:
            answer.append(an)
            an = []
    return answer


