"""def bucket_sort(arr):
    n = len(arr)
    bucket_list = [[] for i in range(n)]
    for value in arr:
        index =int( value * n)
        bucket_list[index].append(value)
    for sub_bucket in bucket_list:
        if len(sub_bucket)>1:
            sub_bucket.sort()
    index = 0
    for i in bucket_list:
        for j in i:
            arr[index] = j
            index+= 1
    print(arr)
arr = [0.34,0.45,0.24,0.50,0.87,0.99]
bucket_sort(arr)




def bucket_sort(arr):
    n = len(arr)
    bucket_list = [[] for i in range(n)]
    min_val = min(arr)
    max_val= max(arr)
    for value in arr:
        index =((value-min_val)* n)//((max_val-min_val)+1)
        bucket_list[index].append(value)
    for sub_bucket in bucket_list:
        if len(sub_bucket)>1:
            sub_bucket.sort()
    index = 0
    for i in bucket_list:
        for j in i:
            arr[index] = j
            index+= 1
    print(arr)
arr = [56,99,456,13,45,67,10]
bucket_sort(arr)

"""

nums = [1, 2, 2, 3, 1, 4, 2, 3, 3]

count = {}
for value in nums:
    if value in count:
        count[value] +=1

    else:
        count[value]=1
        

print(count)
# Output: {1: 2, 2: 3, 3: 3, 4: 1}


#or

nums = [1, 2, 2, 3, 1, 4, 2, 3, 3]

count = {}
for value in nums:
    count[value] =count.get(value,0)+1

print(count)
