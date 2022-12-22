def printTable(S, E, W):
    while S <= E:
        c = 5 * (S - 32) / 9
        print(S, "	", int(c))
        S = S + W


S = int(input())
E = int(input())
W = int(input())
printTable(S, E, W)