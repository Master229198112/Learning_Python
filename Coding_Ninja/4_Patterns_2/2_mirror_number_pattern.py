# Pattern for N = 4
#    1
#   12
#  123
# 1234

n = int(input())
i = 1
while i <= n:
    j = 1
    start_num = 1
    while j <= n - i:
        print(' ', end='')
        j = j + 1
    num = 1
    while num <= i:
        k = i
        print(start_num, end='')
        num = num + 1
        start_num = start_num + 1
    print()
    i = i + 1
