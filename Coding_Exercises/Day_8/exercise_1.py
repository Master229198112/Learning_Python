while True:
    with open(r'E:\Learning\File\coin.txt', 'r') as file:
        coin = file.readlines()

    side = input("Throw the coin and enter head or tail here: ?") + "\n"

    coin.append(side)

    with open(r'E:\Learning\File\coin.txt', 'w') as file:
        file.writelines(coin)

    head = coin.count("head\n")
    percentage = head / len(coin) * 100

    print(f"Heads: {percentage}%")
