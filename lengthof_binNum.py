#length
def count_length(value):
    count =0
    while value>0:
        value = value>>1
        count+=1
    print(count)
count_length(5)



#even or odd

def evenOrodd(value):
    if value&1 == 1:
        print("odd")
    else:
        print("even")
evenOrodd(5)
