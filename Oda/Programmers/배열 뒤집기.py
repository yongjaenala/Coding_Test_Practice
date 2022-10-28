def solution(num_list):
    answer = []
    for i in range(len(num_list)-1, -1, -1):
        answer.append(num_list[i])
    return answer


# def solution(num_list):
#     return num_list[::-1]


# def solution(num_list):
#     num_list.reverse()
#     return num_list