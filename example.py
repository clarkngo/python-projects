import sys

def main():
    validator = [83, 75, 89, 45, 76, 89, 78, 66, 45, 57, 54, 49, 55]
    challenge = sys.argv[1]

    if len(challenge) != len(validator):
        print("Invalid password")
        exit(100)

    x = 0
    while x < len(challenge):
        if ord(challenge[x]) != validator[x]:
            print("Incorrect password")
            exit(200)
        x += 1

    print("Correct password")
    exit(0)

main()