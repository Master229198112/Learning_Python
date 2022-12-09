file = open(r'E:\Learning\File\essay.txt', 'r')
essay = file.read()
file.close()

print(len(essay))


# file = open("essay.txt", 'r')
# content = file.read()
#
# nr_chars = len(content)
# print(nr_chars)
