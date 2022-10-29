def solution(my_string):
    num = [str(n) for n in range(10)]
    answer = []
    for i in my_string :
        if i in num :
            answer.append(int(i))
    return sorted(answer)
