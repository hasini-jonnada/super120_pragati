#for finding first set bin value(1)
def FirstSet_bit(value):
    count =0
    while (value&1==0):
#for finding first reset bin value(0)
    #while (value&1==0):
        value = value>>1
        count+=1
    print(count)
FirstSet_bit(4)       

