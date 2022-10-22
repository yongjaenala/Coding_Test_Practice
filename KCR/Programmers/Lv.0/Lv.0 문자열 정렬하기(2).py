# 첫 번째 풀이
def solution(my_string):
    answer = []
    a = ''
    for i in my_string :
        answer.append(ord(i.lower()))
    answer.sort()
    for i in answer :
        a += chr(i)
    return a

# 두 번째 풀이
def solution(my_string):
    answer = []
    a = ''
    for i in my_string :
        answer.append(i.lower())
    answer.sort()
    return ''.join(answer)