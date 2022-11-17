my = "bus"
answer =''
for i in my:
    if i not in ['i', 'e', 'a', 'o', 'u']:
        answer += i

print(answer)

# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i not in ['i', 'e', 'a', 'o', 'u']:
#             answer += i
#     return answer