def solution(n):
    contain = 0
    multiple = 0
    for i in range(1, n+1) :
        if i%3 == 0 :
            multiple += 1
        na = i%10
        # if na%3 == 0 :
        #     contain += 1
    return n+contain+multiple

n = 15	#25
# n = 40	#76
print(solution(n))