def solution(nums):
    cnt = 0
    for i in range(len(nums)-2) :
        for j in range(1, len(nums)-1) :
            for k in range(2, len(nums)) :
                for l in range(2, i+j+k) :
                    if (i+j+k)%l == 0 :
                        break
                    if l == (i+j+k-1) :
                        cnt += 1
    return cnt

nums = [1,2,3,4]	# 1
nums = [1,2,7,6,4]	# 4
print(solution(nums))