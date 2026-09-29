             "five", "six", "seven", "eight", "nine"]
    
    s = str(num)
    
    # Decide the rules once based on the length 
    even_length = len(s) % 2 == 0
    
    # Which digits stay as digits:
    #   even length -> odd digits stay  (d % 2 == 1)
    #   odd length  -> even digits stay (d % 2 == 0)
    keep_parity = 1 if even_length else 0
    
    # Which case the first copy of each word uses:
    #   even length -> lowercase first (False)
    #   odd length  -> UPPERCASE first (True)
    upper_first = not even_length
    
    # Go through each digit with its position 
    result = ""
    
    # enumerate gives (postion, character), star=1 makes position 1-based
    for p, ch in enumerate(s, start=1):
        d = int(ch) # the digit as int to check odd/even
        
        if d % 2 == keep_parity:
            # digit stay as it is
            result += ch
            
        else:
            # This digit becomes word, exatly p words long
            result += build_word(names[d], p, upper_first)
            
    return result
    
        
    
    
        