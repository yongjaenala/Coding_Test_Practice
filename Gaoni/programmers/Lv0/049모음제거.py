def solution(my_string):
    answer = my_string
    aeiou = ['a', 'e', 'i', 'o', 'u']
    #     for i in range(my_string):
    #         print(i)
    #         # if i not in ['a', 'e', 'i', 'o', 'u']:
    #             # answer = answer + i

    for mo in aeiou:
        answer = answer.replace(mo, '')
    return answer