def solution(num_list):
    num_sum = [x % 2 for x in num_list]

    num_odd = sum(num_sum)
    num_even = len(num_list) - num_odd

    answer = [num_even, num_odd]
    return answer