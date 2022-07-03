import os
filename1 = input("Enter the input file name: ")
file1 = open(filename1, 'r')
print("Name\t:\thours\t:\tSalary")
for line in file1:
     table = line.strip().split(' ')
     if(len(table) == 3):
         wage = float(table[1])
         hours = int(table[2])
         print(table[0], "\t:\t",hours, "\t:\t", wage *  hours)
file1.close()
