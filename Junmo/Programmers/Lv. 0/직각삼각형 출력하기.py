# https://school.programmers.co.kr/learn/courses/30/lessons/120823?language=python3
# 직각삼각형 출력하기

n = int(input())
# print(n)

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()