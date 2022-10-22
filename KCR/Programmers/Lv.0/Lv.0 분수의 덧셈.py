def solution(denum1, num1, denum2, num2):
    n = denum1 * num2 + denum2 * num1
    d = num1 * num2

    for i in range(min(d, n), 1, -1):
        if (n % i == 0) & (d % i == 0):
            n = n // i
            d = d // i
    return [n, d]