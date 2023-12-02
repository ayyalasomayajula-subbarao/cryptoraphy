import math

def is_prime(pr):
    return all(pr % i != 0 for i in range(2, int(math.sqrt(pr)) + 1))

def calculate_d(x, t):
    k = 1
    while True:
        k += t
        if k % x == 0:
            return k // x

def rsa_encrypt(msg, e, n):
    return [(ord(char) ** e) % n for char in msg]

def rsa_decrypt(ciphertext, d, n):
    return ''.join([chr((char ** d) % n) for char in ciphertext])

def main():
    p = int(input("\nEnter first prime number: "))
    if not is_prime(p):
        print("\nWrong input.")
        return

    q = int(input("\nEnter another prime number: "))
    if not is_prime(q) or p == q:
        print("\nWrong input.")
        return

    n = p * q
    t = (p - 1) * (q - 1)

    e = [i for i in range(2, t) if t % i != 0 and is_prime(i) and i != p and i != q]
    d = [calculate_d(x, t) for x in e]

    print("\nPossible values of e and d are:")
    for i in range(len(e)):
        print(f"\n{e[i]}\t{d[i]}")

    msg = input("\nEnter message: ")
    ciphertext = rsa_encrypt(msg, e[0], n)
    print("\nThe encrypted message is:", ciphertext)

    decrypted_msg = rsa_decrypt(ciphertext, d[0], n)
    print("\nThe decrypted message is:", decrypted_msg)

if __name__ == "__main__":
    main()
