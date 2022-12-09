filenames = ["1.doc", "1.report", "1.presentation"]

# This is the syntax of the list comprehension. So it always starts with the new version of each item.
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)
