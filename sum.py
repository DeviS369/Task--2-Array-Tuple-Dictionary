"""
Program 4 : write a python program to find the sum of the first
and last digit of an integer
"""
def sum_first_last_digit(n):
    num_str = str(n)
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    return first_digit + last_digit
number = 12345
result = sum_first_last_digit(number)
print(f"Number: {number}")
print(f"Sum of the first and last digits: {result}")    