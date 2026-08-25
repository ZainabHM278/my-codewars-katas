def mirror(data: list) -> list:
    # the solution goes here
    if not data:
        return []
    
    sorted_lst = sorted(data)
    return sorted_lst + sorted_lst[:-1][::-1]
    
​