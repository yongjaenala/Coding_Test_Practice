
morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
print(type(morse))

#### answer
def solution(letter):
    answer = ''
    letter = letter.split(' ')
    for s in letter:
        answer += morse[s]
    return answer



#####

# letter = ".... . .-.. .-.. ---"
# letter = letter.split(' ')
# print(letter)
#
#
# answer = ''
# for s in letter:
#     answer += morse[s]
#
# print(answer)