fileName = input("Enter the file name: ")
file = open(fileName, 'r')
linecount = 0
for line in file:
    linecount = linecount + 1

print("The number of lines in this txt. file is", linecount)

while True:
    linenum = 0
    num = int(input("Enter a line number: "))
    if num >=1 and num <= linecount:
        file = open(fileName, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                print(lines)
    else:
        if num == 0:
            print("exit to program")
            break
