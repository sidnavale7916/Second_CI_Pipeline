
def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return abs(a)


if __name__ == "__main__":
    print(gcd(12, 18))
    print(gcd(20, 30))
    print(gcd(7, 13))
