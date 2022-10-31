def solution(numbers):
    mx = -100000000
    for i in range(len(numbers)-1) :
        for j in range(i+1, len(numbers)) :
            mx = max(mx, numbers[i]*numbers[j])
    return mx