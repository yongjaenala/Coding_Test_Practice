from string import ascii_lowercase

lower = list(ascii_lowercase)

def solution(age):
    answer = ''
    num_list = list(map(int, str(age)))
    for i in range(len(num_list)):
        answer += lower[num_list[i]]
    return answer

#######
def solution_another(age):
    return ''.join([chr(ord('a')+int(i)) for i in str(age)])