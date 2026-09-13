def transpose_two_strings(arr):
    str1, str2 = arr[0], arr[1]
    max_len = max(len(str1), len(str2))
    
    lines = []
    
    for i in range(max_len):
        char1 = str1[i] if i < len(str1) else ' '
        char2 = str2[i] if i < len(str2) else ' '
        lines.append(f"{char1} {char2}")
    
    return "\n".join(lines)