HEX = set("0123456789ABCDEF")
​
def find_corrupted_byte(dump):
    for index, byte in enumerate(dump):
        if len(byte) != 2:
            return index
        
        for char in byte:
            if char not in HEX:
                return index
    return -1