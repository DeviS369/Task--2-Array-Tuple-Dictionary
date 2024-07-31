"""
Program 3 : Given a python list [10,501,22,37,100,999,85,351]
how many numbers are there in the python list which are happy numbers
"""
def is_happy_number(n):
    def get_next(number):
        return sum(int(char) ** 2 for char in str(number))
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
        return n == 1
def count_happy_numbers(numbers):
        happy_numbers = [num for num in numbers if is_happy_number(num)]
        return len(happy_numbers), happy_numbers
numbers = [10, 501, 22, 37, 100, 999, 85, 351]
count, happy_numbers = count_happy_numbers(numbers)
print(f"Original list: {numbers}")
print(f"Happy numbers: {happy_numbers}")
print(f"Count of happy numbers: {count}")
