def split_by_value(k, elements):
    list1 = [x for x in elements if x < k]
    list2 = [x for x in elements if x >= k]
    
    return list1 + list2 
    #your code here  