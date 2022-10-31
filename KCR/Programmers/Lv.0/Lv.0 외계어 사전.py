def solution(spell, dic):
    same = []
    for i in dic :
        if len(set(i)) == len(spell) :
            same.append(i)
    if len(same) == 0 :
        return 2
    print(same)
    for i in same :
        for j in spell :
            i = i.replace(j, '')
        if len(i) == 0 :
            return 1
    return 2