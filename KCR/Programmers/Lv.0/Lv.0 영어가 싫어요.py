def solution(numbers):
    eng_num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i = 1
    answer = ''
    while len(numbers) != 0 :
        if numbers[0:i] in eng_num :
            answer += str(eng_num.index(numbers[0:i]))
            numbers = numbers[i:]
            i = 1
        else :
            i += 1
    return int(answer)