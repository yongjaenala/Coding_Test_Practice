def solution(my_string):
    answer = ''
    for i, j in enumerate(my_string) :
        if ord(j) <= 90 :
            answer += chr(ord(j)+32)
        else :
            answer += chr(ord(j)-32)
    return answer