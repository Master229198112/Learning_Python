# N = 6
# 123456
#  23456
#   3456
#    456
#     56
#      6
#     56
#    456
#   3456
#  23456
# 123456

n = int(input())
for i in range(1, n + 1):
    count = 1
    for j in range(1, i):
        print(" ", end="")
        count = count + 1
    num = i
    for j in range(count, n + 1):
        print(num, end="")
        num = num + 1
    print()
for i in range(n - 1, 0, -1):
    count = 1
    for j in range(1, i):
        print(" ", end="")
        count = count + 1
    num = i
    for j in range(count, n + 1):
        print(num, end="")
        num = num + 1
    print()
