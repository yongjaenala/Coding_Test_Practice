def solution(n, k):
    price = (12000 * n) + (2000 * k)
    if n >= 10:
        price = price - 2000 * (n // 10)

    return price