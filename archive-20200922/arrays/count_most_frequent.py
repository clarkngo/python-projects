# https://www.codewars.com/kata/56582133c932d8239900002e/train/python

# Find Count of Most Frequent Item in an Array

# Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0

# Example
# input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
# ouptut: 5
# The most frequent number in the array is -1 and it occurs

# Test.assert_equals(most_frequent_item_count([3, -1, -1]), 2, "didn't work for [3, -1, -1]")
# Test.assert_equals(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]), 5, "didn't work for [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]")
# Test.assert_equals(most_frequent_item_count([]), 0, "didn't work for []")
# Test.assert_equals(most_frequent_item_count([9]), 1, "didn't work for [9]")

def most_frequent_item_count(collection):
    if not collection:
        return 0
    from collections import Counter
    data = Counter(collection)
    get_mode = dict(data)
    return max(data.values())

def most_frequent_item_count(collection):
    if collection:
        return max([collection.count(item) for item in collection])
    return 0
