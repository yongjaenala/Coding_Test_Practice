def solution(polynomial):
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
                x += int(i[0])
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

polynomial = "3x + 7 + x"	#"4x + 7"
# polynomial = "x + x + x"	#"3x"
# polynomial = "x + 7 + 15"   #"x + 22"
# polynomial = "3 + 6 + 1"    #"10"
# polynomial = "0"  #0
# polynomial = "6"  #6
# polynomial = "4x"
# polynomial = " " #" "
# polynomial = "x"    #"x"
print(solution(polynomial))
