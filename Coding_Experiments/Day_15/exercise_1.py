import glob

myfiles = glob.glob("E:\Learning\File/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())

# print(myfiles)
