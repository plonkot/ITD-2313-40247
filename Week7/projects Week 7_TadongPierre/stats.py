
lst = [15, 9, 55, 41, 35, 20, 62, 49]

def median(x):
   x = sorted(x)
   listlength = len(x) 
   num = listlength//2
   if listlength%2==0:
       middlenum = (x[num]+x[num-1])/2
   else:
       middlenum = x[num]
   return middlenum

def mean(x):
    sum_of_list = 0
    for i in range(len(x)):
        sum_of_list += x[i]
    average = sum_of_list/len(x)
    return average

def main():
    print("Median of ", lst, " is : ", median(lst))
    print("Mean of ", lst, " is : ", mean(lst))

# The entry point for program execution
if __name__ == "__main__":
    main()
