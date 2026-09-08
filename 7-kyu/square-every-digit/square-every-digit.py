def square_digits(num):
    lst = ""
    for n in str(num):
        lst += str(int(n)*int(n))
        
    return int(lst)
    # Your code here