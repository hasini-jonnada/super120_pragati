#getting the values left to index and making the right as zeroes
def gettingleftofIndex(value,index):
    mask = ~0
    mask = mask<<index
    res = mask& value
    print(res)
gettingleftofIndex(53,3)
