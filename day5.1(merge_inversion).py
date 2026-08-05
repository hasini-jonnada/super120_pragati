"""def merge_sort(nums):
    if len(nums)>1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
       
        while i < len(left) and j < len(right):
            if left[i]<right[j]:
                nums[k] = left[i]
                i+= 1
                k+= 1
            else:
                nums[k] = right[j]
                j+= 1
                k+= 1
                

        while i < len(left):
            nums[k] = left[i]
            i+= 1
            k+= 1
        while j < len(right):
            nums[k] = right[j]
            j+= 1
            k+= 1
                                                                  
nums = [12,14,9,8,5]
merge_sort(nums)
print(nums)

"""





def merge_inversion(nums):
    if len(nums)<=1:
        return 0,nums
    mid = len(nums)//2
    li,left = merge_inversion(nums[:mid])
    ri,right = merge_inversion(numd[mid:])
    mi,merge_list = merge(right,left)
    return merge_list,li+ri+mi


def merge(left,right):
        i=0
        j=0
        merge_list = []
        while i< len(left) and j< len(right):
            if left[i]<right[j]:
                merge_list.append(left[i])
                i+= 1
            else:
                merge_list.append(right[j])
                j+= 1
                mi+= len(left)-i

            merge_list.extend(left[i:])
            merge_list.extend(right[j:])
                return mi,merge_list
nums = [12,14,9,8,5]
sorted_list = merge_inversion(nums)
print(sorted_list)

    
