def partitions(s,e,arr):
    pivot = arr[e]
    i=s
    for j in range(s,e):
        if arr[j]<pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i+= 1
    arr[i],arr[e] = arr[e],arr[i]
    return i
def quick_sort_lomuto(start,end,arr):
    if start<end:
        pivot_location = partitions(start,end,arr)
        quick_sort_lomuto(start,pivot_location-1,arr)
        quick_sort_lomuto(pivot_location+1,end,arr)


arr = [18,45,27,13,25]
quick_sort_lomuto(0,len(arr)-1,arr)
print(arr)
