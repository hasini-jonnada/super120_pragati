def countByAdding1(value):
    count =0
    while value:
        count = count +(value&1)
        value = value>>1
    print(count)
countByAdding1(53)
