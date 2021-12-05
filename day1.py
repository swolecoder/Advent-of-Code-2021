def readFile():
    with open('./input.txt') as file:
        lines = file.readlines()
    return [int(line) for line in lines]



def main():
    data = readFile()
    count = 0
    for i in range(1,len(data)):  
        if data[i] > data[i-1]:
            count +=1

    return count



a = main()
print(a)
            
        
