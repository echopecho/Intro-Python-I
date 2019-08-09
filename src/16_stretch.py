import math

# Determine if an input value is prime
def is_prime(x):
    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
        return True


x = int(input("Enter a number: "))

if is_prime(x):
    print("It is prime")
else:
    print("It is not prime")
