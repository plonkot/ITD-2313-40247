plainText = input("Enter text for encrypt: ")
shift = int(input("Enter the distance value: "))
cipherText = ""
for i in range(len(plainText)):
    char = plainText[i]
    if (char.isupper()):
        cipherText += chr((ord(char) + shift-65) % 26 + 65)
    else:
        cipherText += chr((ord(char) + shift - 97) % 26 + 97)
print("Your ciphertext is: ", cipherText)
