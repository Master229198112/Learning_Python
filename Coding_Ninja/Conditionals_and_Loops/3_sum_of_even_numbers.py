N = int(input())
Sum = 0
for i in range(N, 0, -1):
    if i % 2 == 0:
        Sum = Sum + i
print(Sum)
