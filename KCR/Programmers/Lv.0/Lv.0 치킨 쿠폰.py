def solution(chicken):
    service = chicken//10  # 서비스로 받는 치킨 수
    total = chicken//10 + chicken%10  # 보유 쿠폰 수
    while total >= 10 :
        service += total // 10  # 서비스로 받는 치킨 수
        total = total // 10 + total % 10  # 보유 쿠폰 수
    return service