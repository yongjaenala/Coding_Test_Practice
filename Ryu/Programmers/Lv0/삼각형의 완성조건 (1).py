def solution(sides):
    mx = max(sides)
    Re = sum(sides.remove(max(sides)))
    if mx < Re:
        return 1
    else:
        return 2




sides = [1,2,3]

print(sides.index(max(sides)))
sides.remove((max(sides)))

print(sides)