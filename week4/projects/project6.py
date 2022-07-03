iteration = int(input("Enter number of iteration: "))
presumm = 0
div = 1
sign = True
for i in range(iteration):
    if sign :
        presumm = presumm + 1 / div
    else :
        presumm =  presumm - 1 / div
    div += 2
    sign = not sign
pi = presumm * 4
print("Pi/4 is: ", pi)
