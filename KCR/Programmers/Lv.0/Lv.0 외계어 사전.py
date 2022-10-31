def solution(spell, dic):
    for i in dic :
        if len(i) != len(spell) :
            dic.pop(dic.index(i))
    return dic

spell = ["p", "o", "s"]	; dic = ["sod", "eocd", "qixm", "adio", "soo"]	#2
spell = ["z", "d", "x"]	; dic = ["def", "dww", "dzx", "loveaw"]	#1
spell = ["s", "o", "m", "d"] ; dic = ["moos", "dzx", "smm", "sunmmo", "som"]	#2
print(solution(spell, dic))