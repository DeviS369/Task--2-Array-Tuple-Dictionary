"""
Program 7 : Program for find the non repeating elements in a given list of integers
"""
def find_non_repeating_elements(numbers):
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
            non_repeating_elements = [number for number, count in frequency.items() if count == 1]
            return non_repeating_elements
numbers = [10, 501, 22, 37, 100, 999, 85, 351, 22, 100, 501, 37]
non_repeating_elements = find_non_repeating_elements(numbers)
print(f"List of integers: {numbers}")
print(f"Non-repeating elements: {non_repeating_elements}")