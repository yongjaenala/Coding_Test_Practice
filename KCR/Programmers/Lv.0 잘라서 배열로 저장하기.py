def solution(my_str, n):
    answer = []
    cnt = len(my_str)//n
    for i in range(cnt) :
        answer.append(my_str[i*n:i*n+n])
    if len(my_str)%n != 0 :
        answer.append(my_str[(i+1)*n:])
    return answer