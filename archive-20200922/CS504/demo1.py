num = 3
if num > 0:
    print(num, "is a positive number.")
print("program continues outside if block")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("program continues outside if block")


num = -1
if num > 0:
    print(num, "is a positive number.")
else:
    print(num, "is a negative number.")
print("program continues outside if block")


print("Please Enter an integer number")
num = int(input())

if num > 0:
    print(num, "is a positive number.")
elif num == 0:
    print(num, " is zero.")
else:
    print(num, " is a negative number.")


'''
# Nested if blocks
'''
print("Please Enter an integer number")
num = int(input())

if num >= 0:
    if num == 0:
        print(num, "is zero")
    else:
        print(num, "is a positive number")
else:
    print(num, " is a negative number")


print("Please Enter an integer number")
num = int(input())

if num > 0:
    print(num, "is a positive number")
elif num == 0:
    print(num, "is zero")
else:
    print(num, " is a negative number")


# sum the list of numbers
list_num = [6, 2, 3, 5, 2, 11, 4, 9, 22, -3, 9, 13, 10, 1]
# init. sum
sum = 0
for val in list_num:
    sum = sum + val
print("total sum is ", sum)

sum = 0
for i in range(len(list_num)): # using the range to traverse
    sum = sum + list_num[i]
print("total sum is ", sum)

for i in list_num:
    print(i)
else: # else block
    print("no more item in the list")

# nested loop
for i in range(1,5):
    for j in range(i):
        print(i, end=" ")

# Sum only even numbers, x = user input


list_num = [6, 2, 3, 5, 2, 11, 4, 9, 22, -3, 9, 13, 10, 1]
i = 0
sum = 0
while i < len(list_num): #try while list_num[i]%2 == 0: then fix
    if(list_num[i]%2 == 0):
        sum = sum + list_num[i]
    i = i + 1
print("The total sum of even numbers is ", sum)

i = 0
sum = 0
while i < len(list_num):
    if(list_num[i]%2 == 0):
        sum = sum + list_num[i]
    i = i + 1
# else:
#   i = 0
#   print("Outside while loop and the final sum is ", sum)


# with the user's input character, the program prints a message that says vowel or not. If not vowel, it continues if not, stops.
vowels = "aeiouAEIOU"
#infinite loop
while True:
    v = input("Enter a vowel: ")
    if v in vowels:
        break
    print("No! That's not a vowel. Try again")
    print("You entered ", v)
print("Good job!")


