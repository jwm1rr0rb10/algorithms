def have_opposite_signs(a, b):
    return (a ^ b) < 0

# Examples:
print(have_opposite_signs(5, -3))   # True
print(have_opposite_signs(-7, 12))  # True
print(have_opposite_signs(8, 19))   # False
print(have_opposite_signs(-4, -100))# False