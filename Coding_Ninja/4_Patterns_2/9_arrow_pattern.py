# Note : There is space after every star.
# Pattern for N = 7
# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *

n = int(input())
m = n // 2 + 1
i = 1

while i <= m:
    p = 1
    while p < i:
        print(" ", end="")
        p += 1

    j = i
    c = 1
    while j >= i and c <= i:
        print("* ", end="")
        j += 2
        c += 1

    print()
    i += 1

i = m - 1
while i >= 1:
    p = 1
    while p < i:
        print(" ", end="")
        p += 1

    j = i
    c = 1
    while j >= 1 and c <= i:
        print("* ", end="")
        j = j + 2
        c = c + 1

    print()
    i = i - 1
