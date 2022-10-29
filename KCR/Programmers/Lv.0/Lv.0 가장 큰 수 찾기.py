import numpy as np

def solution(array):
    return [max(array), int(np.argmax(array))]