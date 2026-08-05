def counting_sort(nums):
    max_val = max(nums)
    count = [0]*(max_val +1)
    for i in nums:
        count[i]+= 1 
    #prefix sum
    for i in range(1,len(count)):
        count[i] += count[i-1]
    sorted_list = [0]*len(nums)
    for value in reversed(nums):
        sorted_list[count[value]-1] =value
        count[value]-= 1
    return sorted_list
   
nums = [2,3,1,2,2,3,1,0,1,1,0]
res =counting_sort(nums)
print(res)

