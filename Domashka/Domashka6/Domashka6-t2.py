import os

allFiles = {}

with open('files_size.txt', 'w') as info:
    for roots, dirs, files in os.walk('./..'):
        for file in files:
            path = os.path.join(roots, file)
            size = os.path.getsize(path)
            allFiles[path] = size

    for key, value in allFiles.items():
        info.write(str("File path: '" + key + "' Size: " + str(value) + " bytes\n"))
    biggestFile = max(allFiles, key=allFiles.get)
    print("The biggest file:", biggestFile, "Size:", allFiles[biggestFile], "bytes")

