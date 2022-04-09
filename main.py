def encrypt(string):
    encrypted = ""
    for c in string:
        encrypted += hex(ord(c) ^ 5).replace("0x", "")
    return encrypted

if __name__ == "__main__":
    pre = input("To encrypt: ")
    print("Encrypted:", encrypt(pre))