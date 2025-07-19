def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 1:
        return 0
    else:
        last = n % 10
        remaining = n // 10
        return last + sum_digits(remaining)

print(sum_digits(513))
print(sum_digits(51396))
print(sum_digits(10))
print(sum_digits(0))