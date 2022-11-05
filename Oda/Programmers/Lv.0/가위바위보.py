# 가위 2 바위 0 보 5

def solution(rsp):
    result = ''

    rsp = list(rsp)
    for s in rsp:
        if s == '2':
            result += '0'
        elif s == '0':
            result += '5'
        elif s == '5':
            result += '2'

    return result

# another

def sol(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)
