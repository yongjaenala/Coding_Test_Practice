import numpy as np
def solution(sides):
    mx = sides.pop(np.argmax(sides))
    if mx < sum(sides) :
        return 1
    else :
        return 2