def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last = n // 10
        last = n % 10
        return sum_digits(all_but_last) + last

print(sum_digits(513))