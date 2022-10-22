def solution(A, B):
    for i in range(len(A)):
        if A == B :
            return i
        else :
            A = A[-1]+A[0:-1]  # 마지막 문자 + 나머지 ; hello -> ohell
    return -1