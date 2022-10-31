## 최빈값 구하기

import numpy as np

def solution(array):

    # 한 개의 원소만 가질 시 최빈값은 해당 값.
    if len(array) == 1:
        return array[0]

    # 0으로 초기화 된 리스트 갯수
    # array에서 최댓값 + 1로 배열의 길이 지정 == 인덱스가 각각의 원소값
    list = [0] * (max(array) + 1)


    # 배열의 원소에 해당하는 리스트 인덱스에 증감 +1
    for i in array :
        list[i] += 1

    # list 최대값 인덱스 반환
    mx = int(np.argmax(list))

    # list 최대값을 반환
    mx_v = max(list)

    # 해당하는 인덱스 0으로 초기화
    list[mx] = 0

    # 최빈값이 두개 이상이되면 -1 반환
    # 똑같은 수의 갯수가 같으면 최빈값이 두 개 이상.
    if mx_v == max(list):
        return -1

    return mx