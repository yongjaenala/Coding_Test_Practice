def solution(polynomial):
    if len(polynomial.strip()) == 0 :
        return "0"
    if '+' not in str(polynomial) :
        if 'x' not in str(polynomial) :
            return str(polynomial)
        else :
            return polynomial
    pol = polynomial.split(' + ')
    num = 0
    x = 0
    for i in pol :
        if 'x' in i :
            if len(i) == 1 :
                x += 1
            else :
                x += int(i.replace('x',''))   # i[0] -- x의 계수가 10이상일 경우
        else :
            num += int(i)
    if num == 0 :
        return str(x)+'x'
    if x == 0 :
        return str(num)
    if x == 1 :
        if num == 0 :
            return 'x'
        return 'x + '+str(num)
    if (x == 0) & (num == 0) :
        return "0"
    return str(x)+'x + '+str(num)