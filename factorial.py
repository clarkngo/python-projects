def factorial(num: int) -> int:
    if not ((num >= 0) & (num % 1 == 0)):
      raise Exception(
        f"Number({num}) can't be floting point or negative ")
    return 1 if num == 0 else num * factorial(num - 1)
