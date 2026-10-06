def find_it(seq):
    for i in seq:
        odd_count = seq.count(i)
        if odd_count % 2 != 0:
            return i
​