"""
Program 8 : To find the minimum element in rated and sorted list in python
"""

def find_min_in_rotated_sorted_list(nums):
    left, right = 0, len(nums) - 1
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    if nums[right] >= nums[0]:
        return nums[0]
    while left <= right:    
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
    if nums[mid - 1] > nums[mid]:
        return nums[mid]
    if nums[mid] > nums[0]:
        left = mid + 1
    else:
        right = mid - 1
rotated_sorted_list = [4, 5, 6, 7, 0, 1, 2]
min_element = find_min_in_rotated_sorted_list(rotated_sorted_list)
print(f"Rotated sorted list: {rotated_sorted_list}")
print(f"Minimum element: {min_element}")