def solution(n):
    answer = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j == n:
                answer += 1

    return answer




########

def getMyDivisor(n):
    divisorsList = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ((i ** 2) != n):
                divisorsList.append(n // i)

    divisorsList.sort()

    return divisorsList


# https://minnit-develop.tistory.com/16