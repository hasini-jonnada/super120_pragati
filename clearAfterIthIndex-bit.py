def GettingRightToIth_bit(value,index):
    mask = ~0
    mask = mask>>index
    res = mask&value
    print(res)
GettingRightToIth_bit(21,4)
    
