import math

# Quadratic roots as formulas
def quadratic_roots(a, b, c):
    if a == 0:
        return "Not a quadratic equation."
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        sqrt_d = math.isqrt(discriminant) if discriminant == int(discriminant) else "√({})".format(discriminant)
        return "(-{0} ± {1}) / {2}".format(b, sqrt_d, 2*a)
    else:
        sqrt_d = "i√({})".format(-discriminant)
        return "(-{0} ± {1}) / {2}".format(b, sqrt_d, 2*a)

# Quadratic factorization
def quadratic_factor(a, b, c):
    if a == 0:
        return "Not a quadratic equation."
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Cannot factorize with real numbers."
    sqrt_d = math.isqrt(discriminant) if discriminant == int(discriminant) else None
    if sqrt_d is not None:
        r1 = (-b + sqrt_d) // (2*a)
        r2 = (-b - sqrt_d) // (2*a)
        return "(x-{0})(x-{1})".format(r1, r2)
    else:
        return "Roots are irrational; use quadratic_roots."

# Prime number check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

# GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# LCM of two numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Find all divisors of a number
def divisors(n):
    result = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            result.append(i)
            result.append(-i)
    return "{{{}}}".format("; ".join(map(str, sorted(result))))

# Simple CLI for calculator use
def main():
    print("Math Helper")
    print("1: Quadratic Roots")
    print("2: Quadratic Factorization")
    print("3: Prime Check")
    print("4: GCD")
    print("5: LCM")
    print("6: Divisors")
    print("to exit, enter 'exit'")
    choice = ""
    while choice.strip() != "exit":
        choice = input("Choose a function (1-6): ").strip()
        if choice == "1":
            a, b, c = map(int, input("Enter coefficients like so: 'a b c' ").split())
            print(quadratic_roots(a, b, c))
        elif choice == "2":
            a, b, c = map(int, input("Enter coefficients like so: 'a b c' ").split())
            print(quadratic_factor(a, b, c))
        elif choice == "3":
            n = int(input("Enter a number: "))
            print("Prime" if is_prime(n) else "Not Prime")
        elif choice == "4":
            a, b = map(int, input("Enter two numbers: ").split())
            print("GCD:", gcd(a, b))
        elif choice == "5":
            a, b = map(int, input("Enter two numbers: ").split())
            print("LCM:", lcm(a, b))
        elif choice == "6":
            n = int(input("Enter a number: "))
            print("Divisors:", divisors(n))
        else:
            print("Invalid choice!")

main()
