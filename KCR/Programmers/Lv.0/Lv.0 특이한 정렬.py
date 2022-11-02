def solution(numlist, n):
    for i, j in enumerate(numlist) :
        numlist[i] = (abs(n-j), j)
    numlist.sort(key = lambda x : (x[0], -x[1]))
    answer = []
    for i in numlist :
        answer.append(i[1])
    return answer