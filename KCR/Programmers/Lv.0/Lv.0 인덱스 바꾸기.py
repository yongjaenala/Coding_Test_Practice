def solution(my_string, num1, num2):
    string = []
    for i in my_string :
        string.append(i)
    string[num1], string[num2] = string[num2], string[num1]

    answer = ''
    for i in string :
        answer += i
    return answer