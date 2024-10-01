import math

#*********** LIST OF CODES TO SHOWCASE UNDERSTANDING OF NUMBER THEORY *************



# Function for prime factorisation
def prime_factors(n):
    factors = []
    # Looks for the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # n must be odd, so we check for odd factors
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors

# Euclidean algorithm to find GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Eg
number = 56
print(f"Prime factors of {number}: {prime_factors(number)}")

a = 48
b = 18
print(f"GCD of {a} and {b} using Euclidean algorithm: {gcd(a, b)}")

# base conversion 
def decimal_to_base(n, base):
    if n < 0:
        return "Negative numbers not supported."
    
    if n == 0:
        return "0"

    digits = []
    while n > 0:
        remainder = n % base
        # Convert remainder for bases greater than 10
        if remainder >= 10:
            digits.append(chr(remainder + 55))  # Convert 10-35 to A-Z
        else:
            digits.append(str(remainder))
        n //= base

    # The digits are in reverse order, so we need to reverse them
    digits.reverse()
    return ''.join(digits)


number = 3995
base = 12
converted_value = decimal_to_base(number, base)
print(f"{number} in base {base} is: {converted_value} (base {base})")

# Modular Arithmetic

def mod_add(a, b, m):
    return (a + b) % m

def mod_subtract(a, b, m):
    return (a - b) % m

def mod_multiply(a, b, m):
    return (a * b) % m

def mod_exponentiation(base, exp, m):
    result = 1
    base = base % m
    while exp > 0:
        # If exp is odd, multiply base with result
        if exp % 2 == 1:
            result = (result * base) % m
        # exp must be even now
        exp = exp >> 1  #  exp //= 2
        base = (base * base) % m  # square the base
    return result

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Inverse doesn't exist")
    else:
        return x % m


a = 10
b = 15
m = 6

print("Modular Addition:", mod_add(a, b, m))           # (10 + 15) mod 6
print("Modular Subtraction:", mod_subtract(a, b, m))   # (10 - 15) mod 6
print("Modular Multiplication:", mod_multiply(a, b, m)) # (10 * 15) mod 6
print("Modular Exponentiation:", mod_exponentiation(a, b, m))  # (10^15) mod 6
print("Modular Inverse of a:", mod_inverse(a, m))      # Inverse of 10 mod 6