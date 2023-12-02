import hashlib

def md5(msg):
    md5_hash = hashlib.md5()
    md5_hash.update(msg.encode('utf-8'))
    return md5_hash.digest()

def main():
    msg = "The quick brown fox jumps over the lazy dog"
    
    print("\t MD5 ENCRYPTION ALGORITHM IN PYTHON \n\n")
    print("Input String to be Encrypted using MD5 : \n\t", msg)
    print("\n\nThe MD5 code for input string is: \n\t= 0x", end="")
    
    d = md5(msg)
    for byte in d:
        print("{:02x}".format(byte), end="")
    
    print("\n\n\t MD5 Encryption Successfully Completed!!!\n\n")

if __name__ == "__main__":
    main()
