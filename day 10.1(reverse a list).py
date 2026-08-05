def reverse_list(nums):
    i = 0
    j = len(nums)-1
    while i < j:
        nums[i],nums[j] = nums[j],nums[i]
        i+=1
        j-=1
    return nums
nums = [1,3,6,12,20,25]
res = reverse_list(nums)
print(res)
