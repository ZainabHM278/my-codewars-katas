def multiples(a: int, b: int, limit: int) -> list[int]:
    return [i for i in range(1, limit + 1) if i % a == 0 and i % b == 0]