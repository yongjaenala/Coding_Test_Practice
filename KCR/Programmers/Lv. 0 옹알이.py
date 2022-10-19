def solution(babbling):
    cnt = 0
    for b in babbling :
        for i in ["aya", "ye", "woo", "ma"] :
            if i*2 not in b :
                b = b.replace(i,'')
        if len(b) == 0 :
            cnt += 1
    return cnt