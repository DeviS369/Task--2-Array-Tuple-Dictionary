
"""
Program : 2 Given a python list [10,501,22,37,100,999,85,351]
to count all the prime numbers and create a new python list
which will contain all the prime numbers in it
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_numbers_in_list(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
            return prime_numbers
numbers = [10, 501, 22, 37, 100, 999, 85, 351]
prime_numbers = prime_numbers_in_list(numbers)
print(f"Original list: {numbers}")
print(f"Prime numbers: {prime_numbers}")
print(f"Count of prime numbers: {len(prime_numbers)}")  