import numpy as np
def solution(array):

    a = [0]*(max(array)+1)  # 인덱스 = 숫자 ; 값 = count

    for i in array :
        a[i] += 1
    mx = int(np.argmax(a))  # argmax : 배열에서 최댓값의 인덱스를 반환
    mx_v = max(a)  # 최빈값의 개수
    a[mx] = 0  # 최빈값 개수 초기화
    if mx_v == max(a) :  # 두 번째로 많은 수의 개수와 최빈값 개수 비교
        return -1
    return mx