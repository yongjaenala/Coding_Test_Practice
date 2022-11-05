
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

def sol(array, height):

    return len([i for i in array if i > height])

# wow
def sol_wow(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)