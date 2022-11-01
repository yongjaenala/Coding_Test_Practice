# 아직못품
# https://school.programmers.co.kr/learn/courses/30/lessons/120853
# 컨트롤 제트

def solution(s):
    answer = 0

    sList = s.split()
    for i in range(len(sList) - 1):
        if sList[i + 1] == "Z":
            sList[i] = "0"
    for s in sList:
        try:
            answer += int(s)
        except:
            pass

    return answer

