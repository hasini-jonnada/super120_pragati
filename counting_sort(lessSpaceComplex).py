def counting_sort(nums):
    max_val = max(nums)
    min_val = min(nums)
    count = [0]*((max_val- min_val)+1)
    for value in nums:
        count[value-min_val]+= 1 
    #prefix sum
    for i in range(1,len(count)):
        count[i] += count[i-1]
    sorted_list = [0]*len(nums)
    for value in reversed(nums):
        sorted_list[count[value-min_val]-1] =value
        count[value-min_val]-= 1
    
    return sorted_list
   
nums = [23,18,19,20,23,25,18,20]
res =counting_sort(nums)
print(res)

