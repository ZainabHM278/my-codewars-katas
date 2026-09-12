import math
def solve(s,g):
    if s % g != 0:
        return -1
    a = g
    b = s - g
    if math.gcd(a,b) == g:
        return (a,b)
    
    return -1
        