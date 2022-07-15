def printAll(sequence):
    if sequence:
        print(sequence[0])
        printAll(sequence[1:])

def main():
    seq = "Pierre Tadong"
    printAll(seq)
    
main()
