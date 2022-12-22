# Note: N is always odd.
#
# Pattern for N = 5
#
#   *
#  ***
# *****
#  ***
#   *

n = int(input())
a = (n + 1) // 2
b = n // 2
# First Half
l = 1
while l <= a:
    spaces = 1
    while spaces <= (a - l):
        print(" ", end="")
        spaces += 1
    k = 1
    while k <= (2 * l) - 1:
        print("*", end="")
        k += 1

    print()
    l = l + 1
# Second Half
l = b
while l >= 1:
    spaces = 1
    while spaces <= (b - l + 1):
        print(" ", end="")
        spaces += 1
    k = 1
    while k <= (2 * l) - 1:
        print("*", end="")
        k += 1

    print()
    l = l - 1
