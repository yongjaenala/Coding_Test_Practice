def solution(n, lost, reserve) :
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 경우
    both = set(reserve) & set(lost)
    reserve = list(set(reserve) - both)
    lost = list(set(lost) - both)
    for l in lost :
        if len(reserve) == 0 :
            break
        if l-1 in reserve :
            reserve.remove(l-1)
            n += 1
        elif l+1 in reserve :
            reserve.remove(l+1)
            n += 1
    return n-len(lost)