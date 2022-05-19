def encrypt(string):
    encrypted = [hex(ord(c) ^ 5)[2:] for c in string]
    return "".join(encrypted)

def decrypt(string):
    decrypted = []
    for i in range(0, len(string), 2):
        current = 5 ^ ord(bytes.fromhex(string[i:i+2]).decode())
        decrypted.append(chr(current))
    return "".join(decrypted)

if __name__ == "__main__":
    encrypted = encrypt(input("To encrypt: "))
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypt(encrypted))
