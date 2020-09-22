import random
def securePINGenerator():
    pin = ""
    for i in range(4):
        pin += str(random.randint(0, 9))
    return pin

print("The 4-digit secure PIN is:", securePINGenerator())
