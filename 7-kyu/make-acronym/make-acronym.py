def to_acronym(inp):
    words = inp.split()
    result = "".join(word[0] for word in words)
    
    return result.upper()