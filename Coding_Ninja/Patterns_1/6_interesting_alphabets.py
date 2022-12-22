# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE

n = int(input())
i = 1
k = 1
while i <= n:
    j = 1
    start_char = chr(ord('A') + n - k)
    while j <= i:
        charP = chr(ord(start_char) + j - 1)
        print(charP, end='')
        j = j + 1
    print()
    i = i + 1
    k = k + 1
