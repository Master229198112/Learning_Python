n = int(input())
even = 0
odd = 0
rn = 0

while n > 0:
    r = n % 10

    if r % 2 == 0:
        even = even + r

    else:
        odd = odd + r

    rn = (rn * 10) + r
    n = n // 10

print(even, " ", odd)
