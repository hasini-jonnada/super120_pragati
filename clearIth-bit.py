def clearIth_bit(value,index):
    mask = 1<<index
    mask = ~mask
    res = mask&value
    print(res)
clearIth_bit(5,2)
