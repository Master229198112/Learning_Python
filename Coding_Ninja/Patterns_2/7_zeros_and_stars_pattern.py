# Pattern for N = 4
#
# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000

lines = int(input())
i = 1
j = 1
while i <= lines:
    j = 1
    while j <= lines:
        if i == j:
            print("*", end='')
        else:
            print("0", end='')
        j = j + 1
    j = j - 1
    print("*", end='')
    while j >= 1:
        if i == j:
            print("*", end='')
        else:
            print("0", end='')
        j = j - 1
    print("")
    i = i + 1
