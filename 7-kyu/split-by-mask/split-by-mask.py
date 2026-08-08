def split_by_mask(strng, mask):
    if len(strng) != sum(mask):
        return None
    
    result = []
    start = 0
    
    for length in mask:
        end = start + length 
        result.append(strng[start:end])
        start = end
    
    return result