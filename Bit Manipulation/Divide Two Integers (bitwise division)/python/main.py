def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("division by zero")
    negative = (dividend < 0) != (divisor < 0)
    a, b = abs(dividend), abs(divisor)
    result = 0
    for i in range(31, -1, -1):
        if (a >> i) >= b:
            result += 1 << i
            a -= b << i
    return -result if negative else result

# Examples:
print(divide(13, 3))    # 4
print(divide(-15, 4))   # -3
print(divide(20, -5))   # -4
print(divide(-100, -7)) # 14