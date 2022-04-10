def encrypt(string):
    encrypted = [hex(ord(c) ^ 5)[2:] for c in string]
    return "".join(encrypted)

if __name__ == "__main__":
    pre = input("To encrypt: ")
    print("Encrypted:", encrypt(pre))
