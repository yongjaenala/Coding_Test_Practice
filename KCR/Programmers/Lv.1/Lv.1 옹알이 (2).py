def solution(babbling):
    possible = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for bab in babbling :
        for j in possible :
            if (j in bab) & (j*2 not in bab) :
                bab = bab.replace(j, '0')
                # replace(j, '')를 사용하면 'myea' 같은 경우 답이 다름
        try :
            if int(bab) == 0 :
                cnt += 1
        except :
            pass
    return cnt
