def solution(n):
    na = []
    while n >= 3 :
        na.insert(0, n%3)
        n = n//3
    na.insert(0, n % 3)
    return sum([j*(3**i) for i, j in enumerate(na)])

# 새로 알아가는 int의 기능
# int('숫자(혹은 16진법의 문자와 같은 문자)로 이루어진 문자열',해당 진법) -> 10진법의 수로 변환
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer