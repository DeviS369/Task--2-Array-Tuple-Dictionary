"""
Program 6 : Given three list .taks is to find the duplicates in the three list .
write a python program for the same.you can use your py list
"""
def find_duplicates(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    common_elements = set1 & set2 & set3
    duplicates = list(common_elements)
    return duplicates
list1 = [10, 501, 22, 37, 100, 999, 85, 351]
list2 = [12, 37, 85, 999, 67, 501, 123]
list3 = [501, 37, 999, 85, 78, 22]
duplicates = find_duplicates(list1, list2, list3)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"List 3: {list3}")
print(f"Duplicates in all three lists: {duplicates}")