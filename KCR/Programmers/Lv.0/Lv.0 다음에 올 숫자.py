def solution(common):
    if common[1]-common[0] == common[2]-common[1]:
        return common[-1]+(common[2]-common[1])   # 등차수열
    else :
        return common[-1]*(common[2]/common[1])   # 등비수열