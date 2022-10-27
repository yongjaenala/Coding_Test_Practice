# 미완
# https://school.programmers.co.kr/learn/courses/30/lessons/120863#
# 다항식 더하기

def solution(polynomial):
    answer = ''

    cterm = 0
    xterm = 0
    temp = polynomial.split(' + ')
    for item in temp:
        try:
            if int(item) >= 0:
                cterm += int(item)
        except:
            if item == "x":
                xterm += 1
            else:
                xterm += int(item.replace("x", ""))

    if xterm == 0:
        if cterm == 0:
            answer = "0"
        else:
            answer = str(cterm)
    elif xterm == 1:
        if cterm == 0:
            answer = "x"
        else:
            answer = "x + " + str(cterm)
    else:
        if cterm == 0:
            answer = str(xterm) + "x"
        else:
            answer = str(xterm) + "x + " + str(cterm)

    return answer