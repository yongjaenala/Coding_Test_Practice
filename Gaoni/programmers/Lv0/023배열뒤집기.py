def solution(num_list):
    answer = [num_list[i - 1] for i in range(len(num_list), 0, -1)]

    return answer