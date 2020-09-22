# Dynamic Programming is mainly an optimization over plain recursion.
# Wherever we see a recursive solution that has repeated calls for same inputs,
# we can optimize it using Dynamic Programming. The idea is to simply store the
# results of subproblems, so that we do not have to re-compute them when needed later.
# This simple optimization reduces time complexities from exponential to polynomial.
# For example, if we write simple recursive solution for Fibonacci Numbers, we get
# exponential time complexity and if we optimize it by storing solutions of subproblems,
# time complexity reduces to linear.

# Source: https://www.geeksforgeeks.org/dynamic-programming/

# recursion: exponential
def fib(n):
	if (n <= 1):
		return n
	return fib(n-1) + fib(n-2)

# Fibonacci Series using Dynamic Programming
# Source: https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
def fibonacci(n):

	# Taking 1st two fibonacci nubers as 0 and 1
	FibArray = [0, 1]

	while len(FibArray) < n + 1:
		FibArray.append(0)

	if n <= 1:
		return n
	else:
		if FibArray[n - 1] == 0:
			FibArray[n - 1] = fibonacci(n - 1)

		if FibArray[n - 2] == 0:
			FibArray[n - 2] = fibonacci(n - 2)

	FibArray[n] = FibArray[n - 2] + FibArray[n - 1]
	return FibArray[n]

print(fibonacci(9))
