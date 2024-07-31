"""
Program 5 :A list of N integers which represent the number of mangoes
in a bag .Each bag has a varaiable number of mangoes .
There a M students in Guvi class to distribute the mangoes in such a way
that each student get one bag.The difference between the number of bags
with minimum mangoes given to the student in minimum.
"""

def min_difference_in_mangoes(bags, M):
    bags.sort()
    min_diff = float('inf')
    for i in range(len(bags) - M + 1):
        current_diff = bags[i + M - 1] - bags[i]
        if current_diff < min_diff:
            min_diff = current_diff
            return min_diff
bags = [10, 501, 22, 37, 100, 999, 85, 351]
M = 3
result = min_difference_in_mangoes(bags, M)
print(f"List of mangoes in bags: {bags}")
print(f"Minimum difference between maximum and minimum mangoes in any group of {M} bags: {result}")
