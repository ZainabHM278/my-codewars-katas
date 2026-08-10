def to24hourtime(hour, minute, period):
    # hour will always range from 1 to 12 (inclusive)
    # minute will always range from 0 to 59 (inclusive)
    # period will always be either "am" or "pm"
    if hour < 12 and period == "pm":
        hour += 12
    elif hour == 12 and period == "am": 
        hour = 0
            
    # Format both hour and minute to always have 2 digits
    return f"{hour:02d}{minute:02d}"
​