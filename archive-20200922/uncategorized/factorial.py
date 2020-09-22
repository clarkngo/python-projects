def factorial(num: int) -> int:
    if not ((num >= 0) & (num % 1 == 0)):
      raise Exception(
        f"Number({num}) can't be floting point or negative ")
    return 1 if num == 0 else num * factorial(num - 1)

def factorial2(n:int) -> int:
    factorial = 1
    for i in range (1, n + 1):
        print()
        factorial *= i
    return factorial

print(factorial2(4))