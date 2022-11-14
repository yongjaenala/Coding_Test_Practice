def solution(nums):
    s = []
    for i in range(len(nums)-2) :
        for j in range(i+1, len(nums)-1) :
            for k in range(j+1, len(nums)) :
                s.append(nums[i]+nums[j]+nums[k])
    cnt = 0
    for i in s :
        for j in range(2, i) :
            if i%j == 0 :
                break
            if j == (i-1) :
                cnt += 1
    return cnt