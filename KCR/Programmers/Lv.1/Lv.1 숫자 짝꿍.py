# # 자꾸 런타임 에러 떠서 복잡하게 했다..
# # 첫 번째 풀이
# # def solution(X, Y):
#     x = {}
#     y = {}
#     for i in set(X) :
#         x[i] = X.count(i)
#     for i in set(Y) :
#         y[i] = Y.count(i)
#
#     a = {}
#     for i in x :
#         if i in y.keys() :
#             a[i] = min(x[i], y[i])
#
#     if len(a) == 0 :
#         return '-1'
#     if ('0' in a.keys()) & (len(a) == 1) :
#         return '0'
#
#     a = dict(sorted(a.items(), reverse=True))
#     answer = ''
#     for i in a :
#         answer += i*a[i]
#     return answer
#
# 두 번째 풀이
def solution(X, Y):
    x = list(X.count(str(x)) for x in range(10))
    y = list(Y.count(str(y)) for y in range(10))
    answer = ''
    for i in range(9, -1, -1):
        answer += str(i) * min(x[i], y[i])

    if answer == '':
        return '-1'
    elif answer[0] == "0" and answer[- 1] == "0":
        return "0"
    else:
        return answer
