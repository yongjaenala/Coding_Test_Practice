## 4+5+6 = 4+(4+1)+(4+2) = 4*3 + (1+2) = 15
## 4+5+6+7 = 4+(4+1)+(4+2)+(4+3) = 4*4 + (1+2+3) = 22
# n = 4
def solution(num, total):  # 연속된 수의 개수, 총합
    n = (total-sum(range(1,num)))//num
    return list(range(n,n+num))