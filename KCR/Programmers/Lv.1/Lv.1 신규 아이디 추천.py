# 3자 이상 15자 이하
# 소문자, 숫자, -, _, . 만 사용 가능
# .는 처음과 끝, 연속으로 사용 불가

# 대문자는 소문자로 치환
# 조건에 맞지 않는 문자는 제거
# 처음과 끝에 위치한 .는 제거
# 연속된 .는 하나로 치환
# 빈 문자열이라면 a
# 길이가 16자 이상이면 15자로 자름+마지막이 .이면 . 제거
# 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복

import re
def solution(new_id):
    new_id1 = new_id.lower()
    new_id1 = ''.join(re.findall(r'[a-z0-9\-_.]+', new_id1))
    new_id1 = re.sub(r'[\.]+',".",new_id1)

    while (new_id1[0] == '.') | (new_id1[-1] == '.') :
        if new_id1[0] == '.' :
            new_id1 = new_id1[1:]
        elif new_id1[-1] == '.' :
            new_id1 = new_id1[0:-1]
        if len(new_id1) == 0 :
            new_id1 = 'a'
    if len(new_id1) <= 2 :
        return new_id1+new_id1[-1]*(3-len(new_id1))
    elif len(new_id1) >= 15 :
        new_id1 = new_id1[:15]
        while new_id1[-1] == '.' :
            new_id1 = new_id1[:-1]
        return new_id1
    else :
        return new_id1


# ...!@BaT#*..y.abcdefghijklm
# 대문자 치환
# ...!@bat#*..y.abcdefghijklm
# 조건에 맞지 않는 문자 제거
# ...bnew..y.abcdefghijklm
# 처음과 끝에 위치한 . 제거
# bnew..y.abcdefghijklm
# 중복된 . 하나로 치환
# bnew.y.abcdefghijklm
# 길이가 19로 15이상이므로 뒤에 문자 제거
# bnew.y.abcdefghi
new_id = "...!@BaT#*..y.abcdefghijklm"	# "bat.y.abcdefghi"
# new_id = "z-+.^."	# "z--"
# new_id = "=.="	# "aaa"
# # new_id = "123_.def"	# "123_.def"
# # new_id = "abcdefghijklmn.p"	# "abcdefghijklmn"
print(solution(new_id))


# 정규식 숙지 필요!!
# 다른 풀이
import re
def solution(new_id):
    new = new_id
    new = new.lower()
    new = re.sub('[^a-z0-9\-_.]', '', new)
    new = re.sub('\.+', '.', new)
    new = re.sub('^[.]|[.]$', '', new)
    new = 'a' if len(new) == 0 else new[:15]
    new = re.sub('^[.]|[.]$', '', new)
    new = new if len(new) > 2 else new + "".join([new[-1] for i in range(3-len(new))])
    return new