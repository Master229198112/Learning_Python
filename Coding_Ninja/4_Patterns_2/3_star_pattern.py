# Pattern for N = 4
#
#    *
#   ***
#  *****
# *******

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
        print("*", end='')
        num = num + 1
        start_num = start_num + 1
    start_num = i - 1
    while start_num >= 1:
        print("*", end='')
        start_num = start_num - 1
    print()
    i = i + 1
