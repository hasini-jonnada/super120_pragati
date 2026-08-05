def extract_bit(value,index):
    mask = 1<<index
    res = value & mask
    if res == 0:
        print(0)
    else:
        print(1)
extract_bit(5,1)
