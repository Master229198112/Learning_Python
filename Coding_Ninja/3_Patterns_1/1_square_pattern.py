# Pattern for N = 4
# 4444
# 4444
# 4444
# 4444

n = int(input())

r = 1

while r <= n:
    c = 1

    while c <= n:
        print(n, end='')
        c += 1

    print()
    r += 1
