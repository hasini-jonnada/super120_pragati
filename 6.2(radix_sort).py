def counting_sort(nums,digit):
    count = [0]*10
    for value in nums:
        index = (value//digit)%10
        count[index]+= 1
    for i in range(1,len(count)):
        count[i] += count[i-1]
    res = [0]*len(nums)
    for value in reversed(nums):
        digit_val = (value//digit)%10
        res[count[digit_val]-1] = value
        count[digit_val]-= 1
    return res

def radix(nums):
    max_value = max(nums)
    digit = 1  
    while max_value//digit >0:
        nums = counting_sort(nums,digit)
        digit = digit*10
    return nums   
    
nums = [125,15,18,7,456]
res =radix(nums)
print(res)
