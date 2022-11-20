def solution(arr, divisor):
    div = []
    for i in arr :
        if i%divisor == 0 :
            div.append((i//divisor, i))
    return ([-1] if len(div) ==0 else [a[1] for a in sorted(div)])

# 다른 풀이
def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]

# True일 때 or 앞에 값 출력 False면 뒤에 값 출력
# 값이 있으면 True, 없으면 False