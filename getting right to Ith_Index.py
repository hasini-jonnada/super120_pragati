#getting the values right to index and making the left as zeroes
print(bin(13))
def GettingRightToIth_bit(value,index):
    mask = 1<<index
    mask = mask-1
    res = mask&value
    print(res)
GettingRightToIth_bit(58,3)
    
