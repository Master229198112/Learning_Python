# Pattern for N = 4
# 4444
# 333
# 22
# 1

n = int(input())
i = 1
k = n
while i <= n:
    j = 1
    while j <= n - i + 1:
        print(k, end='')
        j = j + 1
    print()
    i = i + 1
    k = k - 1
