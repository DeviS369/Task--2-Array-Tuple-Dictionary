"""
Program 9 : Given a python list [10,20,30,9] and a value 59 ,
write a python program to find a triblet in the list whose sum is equal to the
given value
"""

def find_triplet_with_sum(nums, target_sum):
    n = len(nums)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target_sum:
                    return (nums[i], nums[j], nums[k])
        return None
numbers = [10, 20, 30, 9]
target_sum = 59
triplet = find_triplet_with_sum(numbers, target_sum)
if triplet:
    print(f"Triplet found: {triplet}")
else:
    print("No triplet found with the given sum.")