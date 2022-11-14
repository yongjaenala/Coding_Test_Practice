# def solution(numbers, k):
#
#     even = [i for i in range(1000) if i % 2 == 0]
#
#     num_in = even[k]%len(numbers)
#
#     answer = numbers[num_in]
#     return answer
def solution(numbers, k):

    num_in = ((k-1)*2)%len(numbers)

    answer = numbers[num_in]

    return answer

even = [i for i in range(1000) if i % 2 == 0]
print(even)

print(solution([1, 2, 3, 4], 2))
