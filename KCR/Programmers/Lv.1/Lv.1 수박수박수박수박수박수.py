def solution(n):
    return ('수박'*(n//2+1))[:n]
    # return ('수박'*n)[:n]  -- 이걸로 해도 runtime 에러 안 나넹..