def power(a, b, mod):
    if b == 1:
        return a
    t = power(a, b // 2, mod)
    if b % 2 == 0:
        return (t * t) % mod
    else:
        return (((t * t) % mod) * a) % mod

def calculate_key(a, x, n):
    return power(a, x, n)

def main():
    n = int(input("Enter the value of n: "))
    g = int(input("Enter the value of g: "))

    x = int(input("Enter the value of x for the first person: "))
    a = power(g, x, n)

    y = int(input("Enter the value of y for the second person: "))
    b = power(g, y, n)

    key_first_person = power(b, x, n)
    key_second_person = power(a, y, n)

    print("Key for the first person is:", key_first_person)
    print("Key for the second person is:", key_second_person)

if __name__ == "__main__":
    main()
