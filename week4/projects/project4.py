height = float(input("Enter the height: "));
nbreBouns = int(input("Enter number of bouncing: "))

y = height
sum = 0
for count in range(0, nbreBouns):
    sum += y + 0.6 * y
    y = 0.6 * y
print("Distance is: ", sum)
