contents = ["All carrots to be sliced longitudinally.", "The carrots were reportedly sliced",
            "The slice process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filenames in zip(contents, filenames):
    file = open(f"E:\Learning\File\{filenames}", 'w')
    file.write(content)

a = "So if the string is outside of the list, a backslash is used. " \
    "Additionally, both parts of the string are still. Enclosed in quotes both. " \
    "There is a backslash in the first line, and if you want to keep splitting, " \
    "you want to add another backslash and the " \
    "other part of the string there and so on."
