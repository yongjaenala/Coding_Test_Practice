def solution(chicken):
    service = chicken//10
    total = chicken//10 + chicken%10
    while total >= 10 :
        service += total // 10
        total = total // 10 + total % 10
    return service