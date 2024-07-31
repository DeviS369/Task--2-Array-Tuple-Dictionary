"""
Program 10 : Given a list [4,2,-3,1,6] .
write a python program to find if there is a sub list with sum equal to zero
"""

def has_zero_sum_sublist(nums):
    cumulative_sums = set()
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum == 0 or current_sum in cumulative_sums:
            return True
        cumulative_sums.add(current_sum)
        return False
numbers = [4, 2, -3, 1, 6]
result = has_zero_sum_sublist(numbers)
if result:
    print("There is a sublist with sum equal to zero.")
else:
    print("There is no sublist with sum equal to zero.")
