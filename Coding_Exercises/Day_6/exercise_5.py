file = open(r'E:\Learning\File\a.txt', 'r')
a = file.readline()
file.close()
print(a)

file = open(r'E:\Learning\File\b.txt', 'r')
a = file.readline()
file.close()
print(a)

file = open(r'E:\Learning\File\c.txt', 'r')
a = file.readline()
file.close()
print(a)


# filenames = ['a.txt', 'b.txt', 'c.txt']
#
# for filename in filenames:
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)
