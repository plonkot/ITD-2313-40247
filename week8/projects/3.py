import math

TOLERANCE = 0.000001
def newton(x, estimate):
    difference = abs(x - estimate ** 2)
    if difference <= TOLERANCE:
        return estimate
    else:
        return newton(x, (estimate + x / estimate) / 2)

def main():
    while True:
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
            break
        x = float(x)
        print("The program's estimate is", newton(x, 1))
        print("Python's estimate is ", math.sqrt(x))

if __name__ == "__main__":
    main()
