# 첫 번째 풀이
# def solution(numbers, k):
#     num = 0
#     if k == 1 :
#         return numbers[0]
#     for i in range(2, k+1) :
#         num += 2
#         if num >= len(numbers) :
#             num -= len(numbers)
#         answer = numbers[num]
#     return answer

# 두 번째 풀이
def solution(numbers, k):
    return 2 * (k - 1) % numbers[-1] + 1