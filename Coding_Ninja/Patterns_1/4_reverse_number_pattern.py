# Pattern for N = 4
# 1
# 21
# 321
# 4321

n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print((i + 1) - j, end='')
        j = j + 1
    print()
    i = i + 1
