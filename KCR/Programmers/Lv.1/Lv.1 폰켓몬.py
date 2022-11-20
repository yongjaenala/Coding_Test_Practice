# 첫 번째 풀이
def solution(nums):
    num = set(nums)
    get = len(nums)//2
    if get <= len(num) :
        return get
    else :
        return len(num)

# 두 번째 풀이
def solution(nums) :
    return min(len(set(nums)), len(nums)/2)