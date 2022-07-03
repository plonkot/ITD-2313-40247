salary = int(input("Enter salary: "))
total = salary
for i in range(1, 9, 1):
    total +=  (2 /100) * total
print("Total salary after 10 years: ", round(total,2))
