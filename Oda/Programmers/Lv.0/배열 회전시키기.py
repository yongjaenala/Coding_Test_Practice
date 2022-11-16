def solution(numbers, direction):
    answer = []
    return answer

direction = 'left'
numbers = [1, 2, 3]
# left -1 , right +1

# temp = numbers[i]

if direction == 'right':
    answer = [numbers[-1]]
    for i in range(len(numbers)-1):
        answer.append(numbers[i])
elif direction == 'left':
    answer = [numbers[1]]
    for i in range(2, len(numbers)):
        answer.append(numbers[i])
    answer.append(numbers[0])

print(answer)

def sol(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]