def solution(babbling):
    cnt = 0
    for b in babbling :
        for i in ["aya", "ye", "woo", "ma"] :
            if i*2 not in b :  # 연속하는지 확인
                b = b.replace(i,'')
        if len(b) == 0 : # 문자열이 끝났는지 확인
            cnt += 1
    return cnt