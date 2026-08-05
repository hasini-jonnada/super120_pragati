def flipIth_bit(value,index):
    mask = 1<<index
    res = mask ^ value
    print(res)
flipIth_bit(5,3)
