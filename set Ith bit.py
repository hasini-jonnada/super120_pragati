def setIth_bit(value,index):
    mask = 1<<index
    res = value | mask
    if res == 0:
        print(0)
    else:
        print(1)
setIth_bit(5,1)
