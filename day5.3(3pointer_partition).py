def _3way_partition(start,end,arr):
    if start<end:
        pivot = arr[end]
        lp =start
        i = start
        hp = end
        while i <= hp:
            if arr[i] > pivot:
                arr[i],arr[hp] = arr[hp],arr[i]
                hp -= 1
            elif arr[i]<pivot:
                arr[i],arr[lp] = arr[lp],arr[i]
                lp+=1
                i+= 1
            else:
                i+= 1
        _3way_partition(start,lp-1,arr)
        _3way_partition(hp+1,end,arr)


arr=[12,14,9,8,5,9,14,12]
_3way_partition(0,len(arr)-1,arr)
print(arr)                
  """      
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
       
     #   Do not return anything, modify nums in-place instead.
      #  Recursive 3-way partition
        
        def helper(low, mid, high, nums):
            if mid > high:   # base case
                return

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                helper(low + 1, mid + 1, high, nums)
            elif nums[mid] == 1:
                helper(low, mid + 1, high, nums)
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                helper(low, mid, high - 1, nums)

        helper(0, 0, len(nums) - 1, nums)
