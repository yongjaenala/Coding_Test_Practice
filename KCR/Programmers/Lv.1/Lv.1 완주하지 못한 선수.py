def solution(participant, completion):
    dic = {}
    for one in participant:
        if dic.get(one):
            dic[one] += 1
        else:
            dic[one] = 1

    for one in completion:
        dic[one] -= 1

    for key in dic:
        if dic[key] > 0:
            return key