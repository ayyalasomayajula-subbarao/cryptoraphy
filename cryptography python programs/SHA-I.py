import hashlib

def sha1_hash(input_str):
    sha1 = hashlib.sha1()
    sha1.update(input_str.encode())
    return sha1.hexdigest()

def main():
    try:
        md = hashlib.sha1()
        print("Message digest object info:")
        print(" Algorithm =", md.name)
        print(" ToString =", md.hexdigest())

        input_str = ""
        md.update(input_str.encode())
        output = md.digest()
        print("\nSHA1(\"" + input_str + "\") =", output.hex())

        input_str = "abc"
        md.update(input_str.encode())
        output = md.digest()
        print("\nSHA1(\"" + input_str + "\") =", output.hex())

        input_str = "abcdefghijklmnopqrstuvwxyz"
        md.update(input_str.encode())
        output = md.digest()
        print("\nSHA1(\"" + input_str + "\") =", output.hex())

    except Exception as e:
        print("Exception:", e)

if __name__ == "__main__":
    main()
