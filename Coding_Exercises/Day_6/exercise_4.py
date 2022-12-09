filename = ["1.txt", "2.txt", "3.txt"]

for filename in filename:
    file = open(f"E:\Learning\File\{filename}", 'w')
    file.write("Hello")
    file.close()


# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for filename in filenames:
#     file = open(filename, 'w')
#     file.write("Hello")
#     file.close()
