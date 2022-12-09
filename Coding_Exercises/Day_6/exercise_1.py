file = open(r'E:\Learning\File\essay.txt', 'r')
essay = file.readlines()
file.close()

for index, item in enumerate(essay):
    row = f"{index + 1}-{item}"
    print(row.title())


# file = open("essay.txt", 'r')
# content = file.read()
# print(content.title())
