# 첫 번째 풀이
def solution(age):
    eng_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    for i in str(age) :
        a_age = ''
        for i in str(age) :
            a_age += eng_list[int(i)]
        return a_age

# 두 번째 풀이
from string import ascii_lowercase

def solution(age):
    a_age = ''
    eng_list = list(ascii_lowercase[:10])
    for i in str(age) :
        a_age += eng_list[int(i)]
    return a_age