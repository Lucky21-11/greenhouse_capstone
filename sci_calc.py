#ARYAN SHARMA 16015025070
def power(a, b):
    return a ** b


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    assert power(2, 3) == 8
    assert factorial(5) == 120
    assert gcd(12, 18) == 6
    assert is_prime(7) == True

    print("All self-tests passed!")