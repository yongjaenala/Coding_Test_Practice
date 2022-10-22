def solution(array): # array의 길이는 홀수
    array.sort()
    return array[len(array)//2]