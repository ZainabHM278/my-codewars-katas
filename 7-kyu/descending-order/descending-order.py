def descending_order(num):
    lst = [int(x) for x in str(num)]
    lst.sort(reverse=True)
    return int("".join(map(str,lst)))