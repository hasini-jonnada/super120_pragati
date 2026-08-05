"""def binary_search(arr,key):
    n = len(arr)-1
    low = 0
    high =n
    while low<= high:
        mid = (low+high)//2
        if arr[mid]== key:
            return mid
        elif key < arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1
 
arr = [2,5,8,10,15,20]
res =binary_search(arr,15)
print(res)




#first and last occurance using binary search
def binary_search(arr,key):
    n = len(arr)-1
    low = 0
    high =n
    while low<= high:
        mid = (low+high)//2
        if arr[mid]== key:
            res = mid
            high= mid-1
        elif key < arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return res
arr = [1,2,3,3,3,4,5]
res =binary_search(arr,3)
print(res)



def binary_search(arr,key):
    n = len(arr)-1
    low = 0
    high =n
    while low<= high:
        mid = (low+high)//2
        if arr[mid]== key:
            res = mid
            low= mid+1
        elif key < arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return res
arr = [1,2,3,3,3,4,5]
res =binary_search(arr,3)
print(res)


#floor and ceil using binarysearch
def ceil(arr,key):
    n = len(arr)-1
    low = 0
    high =n
    while low<= high:
        mid = (low+high)//2
        if arr[mid]>key:
            res = mid
            high= mid-1
        else:
            low = mid+1
            
    return res
arr = [1,2,3,4,5,7,9]
res =ceil(arr,7)
print(res)


def floor(arr,key):
    n = len(arr)-1
    low = 0
    high =n
    while low<= high:
        mid = (low+high)//2
        if key >arr[mid]:
            res = mid
            low = mid+1
        else:
            high =mid-1
            
    return res
arr = [1,2,3,4,5,7,9]
res =floor(arr,7)
print(res)


"""




def floor(arr):
    n = len(arr)-1
    low = 0
    high =n
    while low<high:
        mid = (low+high)//2
        if arr[mid]>=arr[mid+1]:
            res = arr[mid]
            high= mid
        else:
            low=mid+1            
    return res
arr = [1,2,3,4,5,9,7]
res = floor(arr)
print(res)














