def solution(X, Y):
    answer = []
    # Y의 길이가 항상 X보다 길게 만들기
    if len(X) > len(Y) :
        X, Y = Y, list(X)
    else :
        Y = list(Y)

    for i in X:
        try :
            answer.append(Y.pop(Y.index(i)))
        except :
            pass
    answer.sort(reverse=True)

    ans = ''
    for i in answer :
        ans += i
    if ans == '' :
        return '-1'
    else :
        if int(ans) == 0 :
            return '0'
        return ans

X = "100" ; Y = "2345"    #"-1"
# X = "100" ; Y = "2?03045"  #  "0"
# X = "100" ; Y = "123450"  #  "10"
# X = "12321" ; Y = "42531"  #  "321"
# X = "5525" ; Y = "1255"    #"552"
print(solution(X, Y))