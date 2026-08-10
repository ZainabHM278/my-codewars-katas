def introverted_seat(seats: str) -> str | None:
    best_seat = None 
    min_threats = 2 # threats must be less than this
    
    for idx, seat in enumerate(seats):
        if seat == "0":
            # count threats of the left (idx - 1) and on the right (idx +1)
            left_threat = 1 if (idx > 0 and seats[idx - 1] in "01") else 0
            right_threat = 1 if (idx < len(seats) - 1 and seats[idx + 1] in "01") else 0 
            
            total_threats = left_threat + right_threat
            
            # check if the seat is valid ( < 2 thrats) and better than previous seat
            if total_threats < min_threats:
                min_threats = total_threats
                best_seat = idx
                
                # if we find 0 threats, we can stop searching
                if min_threats == 0:
                    break
                    
    if best_seat is None:
        return None
    
    return seats[:best_seat] + "1" + seats[best_seat + 1:]
        
                
                