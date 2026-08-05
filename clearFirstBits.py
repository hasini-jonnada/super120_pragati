#making the values as zeroes from starting 
def clearStarting_bit(value,index):
    count =0
    temp = value
    while temp>0:
        temp = temp>>1
        count+=1
    mask = 1<<(count-index)
    mask = mask-1
    res = mask & value
    print(res)
clearStarting_bit(53,2)
    
