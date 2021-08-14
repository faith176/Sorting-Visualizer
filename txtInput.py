
def readFile(elements):
    print("Each element to sort should be on a separate line in the file")
    filePath = input("Enter file path: ")
    values = []
    with open(filePath) as f:
        line = f.readline()
        count = 0
        while line:
            count += 1
            line = f.readline()
            if count < elements:
                values.append(int(line.strip("\n")))
    print(values)
    return values


