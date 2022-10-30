def solution(array):
    answer = 0
    for j in array:
        if int(j % 10) == 7:
            j = j / 10
            answer += 1
        elif int(j / 10) < 0:
            break
    return answer

array = [7,77,17]
print(solution(array))
print(7%10)