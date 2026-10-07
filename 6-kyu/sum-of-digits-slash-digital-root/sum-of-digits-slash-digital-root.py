def digital_root(n):
    return n if n == 0 else 1 + (n - 1) % 9
            