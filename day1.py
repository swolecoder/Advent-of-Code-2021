def readFile(textFile):
    with open(textFile) as file:
        lines = file.readlines()
    return [int(line) for line in lines]


# first part
def first_part():
    data = readFile('./firstFile.txt')
    count = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            count += 1

    return count

# second part


def second_part():
    data = readFile('./secondFile.txt')

    windowSize = 3

    runningSum = sum(data[:3])
    index = 0
    previousSum = runningSum
    count = 0

    for i in range(3, len(data)):
        runningSum -= data[index]
        runningSum += data[i]
        if runningSum > previousSum:
            count += 1

        previousSum = runningSum
        index += 1

    return count


a = second_part()  # main()
print(a)
