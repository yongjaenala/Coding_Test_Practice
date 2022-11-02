def solution(array):
    if len(array) % 2 == 0:
        return array[len(array)//2]
    else:
        return array[len(array)//2-1]


# array = [1,2,7,10,11]]
array = [9, -1, 0,1]
print(len(array)/2)
print(solution(array))