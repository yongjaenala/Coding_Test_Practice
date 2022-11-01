def solution(my_string):
    h = 0
    i = 1
    num = 0
    while len(my_string) != 0:
        try:
            num = int(my_string[0:i])
            i += 1
        except :
            h += num
            my_string = my_string[i:]
            i = 1
            num = 0
        if (len(my_string[0:i-1]) == len(my_string)) :  # 숫자로 끝나는 경우 무한 루프 도는 것을 방지
            h += num
            break
    return h