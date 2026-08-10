def to_12_hour_time(time_string):
    # The timestring will always be four digits using
    # "hhmm" format.
    # return 'h:mm am' or 'h:mm pm'
    hours = int(time_string[:2])
    mins = time_string[2:]
    period = "pm" if hours >= 12 else "am"
    
    if hours == 0 or hours == 12:
        hours = 12
    elif hours > 12:
        hours = hours - 12
    
    return f"{hours}:{mins} {period}"
        
        
        
​