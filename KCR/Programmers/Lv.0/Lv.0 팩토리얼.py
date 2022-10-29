import math
def solution(n):
    i = 1
    while True :
        if (math.factorial(i) <= n) & (math.factorial(i+1) > n) :
            return i
        i += 1