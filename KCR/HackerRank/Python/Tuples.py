if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))

# 2
# 1 2

# result : 3713081631934410656