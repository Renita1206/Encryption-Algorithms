def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += str(chr((ord(char) + s-65) % 26 + 65))
        else:
            result += str(chr((ord(char) + s - 97) % 26 + 97))
    return result

key = int(input("Enter a key: "))

while(1):
    message = input("Enter message to encrypt: ")
    print(encrypt(message, key))
    code = input("Enter code to be decrypted: ")
    print(encrypt(code,26-key))

