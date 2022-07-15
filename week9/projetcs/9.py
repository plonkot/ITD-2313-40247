def getNumberList(filename):
    with open(filename,'r') as f:
        strList = f.read().split('\n')
        numberList = [int(num) for num in strList]
    return numberList

def getAverage(filename, func):
    numbers = func(filename)
    return sum(numbers)/len(numbers)

def main():
    filename = input("Input the file name: ")
    average = getAverage(filename, getNumberList)
    print(average)

if __name__ == "__main__":
    main()
