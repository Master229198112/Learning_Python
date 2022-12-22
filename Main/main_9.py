n = int(input())

currRow = 1

while currRow <= n:
    currCol = 1

    while currCol <= n:
        print(n, end='')
        currCol += 1

    print()
    currRow += 1
