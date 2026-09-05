def collision(x1, y1, radius1, x2, y2, radius2): 
    distance_x = x2 - x1
    distance_y = y2 - y1
    
    distance_squared = distance_x ** 2 + distance_y ** 2
    
    radii_sum_squared = (radius1 + radius2) ** 2
    
    return distance_squared <= radii_sum_squared