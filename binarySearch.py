"""
Function to check whether entered element is present in the list or not
"""


def binary_search(arr, item):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = (first + last) // 2  # Check if element is present at the mid-index or not
        if arr[mid] == item:
            return True
        elif item < arr[mid]:
            last = mid - 1  # if not then loop will continue
        else:
            first = mid + 1  # It will generate a number which is greater than index value of list
    return False


word = ["apple", "banana", "mango", "kiwi", "pineapple"]  # list of words
name = input("enter name : ")
result = binary_search(word, name)
if not result:
    print("Element not found")
else:
    print(f"Element found")
