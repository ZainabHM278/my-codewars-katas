def words_to_marks(s):
    total_score = 0
    
    for char in s:
        value = ord(char) - 96
        total_score += value
        
    return total_score