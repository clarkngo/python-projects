# https://www.hackerrank.com/challenges/no-idea/problem

# Create a program that takes in 4 inputs from the user:
#   1st input: The length of an integer array N and length of both          sets A and B, separated by a space
#   2nd input: The integers for the array N, separated by spaces
#   3rd input: The integers for set A, separated by spaces
#   4th input: The integers for set B, separated by spaces

# Output a single integer, your total happiness
#   happiness is increased whenever an element of set A is found on   #   array N and is decreased whenever an element of set B is found    #   on array N


# The first line contains integers 'n' and 'm' separated by a space.
usr_in1 = input().split(' ', 1) # expecting two integers only

# The second line contains 'm' integers, the elements of the array.
nums = input().split(' ')
nums = list(map(int, nums))

# The third and fourth lines contain 'm' integers, 'A' and 'B', respectively.
set_A = input().split(' ')
set_B = input().split(' ')

# convert elements to int and transform to set
set_A = set(map(int, set_A))
set_B = set(map(int, set_B))

# start counting happiness!
happiness = 0
for i in range(len(nums)):
    if nums[i] in set_A:
        happiness += 1
    elif nums[i] in set_B:
        happiness -= 1
print(happiness)
