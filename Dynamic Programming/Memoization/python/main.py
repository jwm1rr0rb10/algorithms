# With memoization (inefficient):


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


# With memoization (efficient):


def fib(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]