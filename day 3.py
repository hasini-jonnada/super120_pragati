""" 
#1 t0 N and N to 1
def rec(n):
    if(n != 0):
        print(n)
        rec(n-1)
        print(n)
rec(5)
        
 
   
    
def rec(n):
    if(n <= 5):
        print(n)
        rec(n+1)
        print(n)
rec(1)




def rec(n):
    if(n != 0):
        
        rec(n-1)
        print(n)
rec(5)




def rec(n):
    if(n <= 5):
        print(n)
        rec(n+1)
        
rec(1)
 

#with return key

def rec(index,n):
    if index == n+1:
        return
    print(index,end = " ")
    rec(index+1,n)
rec(1,5)



def even_rec(index,n):
    while index <= n+1:
        if index %2 == 0:
            print(index)
        even_rec(index+1,n)
          
even_rec(1,10)        





def odd_rec(index,n):
    while index < n+1:
        if index %2 == 1:
            print(index)
        even_rec(index+1,n)
        return  
odd_rec(1,10) 


def evenrec(n):
    if n < 0:
        return
    print(n)
    evenrec(n-2)
evenrec(10)




def evenrec(n):
    if n < 0:
        return
    print(n)
    evenrec(n-2)
n = 25
evenrec(n-1 if n%2 == 0 else n)



#sum of n values
def sum_N_values(n):
    
     if n==1:
        return 1
     return n + sum_N_values(n-1)
res = sum_N_values(5)
print(res)

       


#factorial
def fac(n):
    if n==1:
        return 1
    return n * fac(n-1)
res = fac(5)
print(res)




#sum of values in list
def sum_of_given_list(index, nums,n):
    if index == n:
        return 0
    return nums[index] + sum_of_given_list(index+1, nums,n)    
nums = [2,3,4,5,6]
res = sum_of_given_list(0,nums,len(nums))    
print(res)    



#sum of values in list
def sum_of_given_list_slicing(nums):
    if len(nums)==1:
        return nums[0]
    return nums[0] + sum_of_given_list_slicing(nums[1:])    
nums = [2,3,4,5,6]
res = sum_of_given_list_slicing(nums)    
print(res)




#palindrome
def palindrome(left,nums,right):
    if left >= right:
        return "palindrome"
    if nums[left] != nums[right]:
        return "not palindrome"
    return palindrome(left+1,nums,right-1)
nums = [2,4,5,4,2]
res = palindrome(0,nums,len(nums)-1)
print(res)



#min value in list 
def find_min(index,nums):
    if index == len(nums)-1:
        return nums[index]
    if nums[index]< find_min(index+1,nums):
        return nums[index]
    else:
        return find_min(index+1,nums)
    
nums = [2,5,7,3,1]
res = find_min(0,nums)
print(res)



#max value in a list
def find_min(index,nums):
    if index == len(nums)-1:
        return nums[index]
    if nums[index]> find_min(index+1,nums):
        return nums[index]
    else:
        return find_min(index+1,nums)
    
nums = [2,5,7,3,1]
res = find_min(0,nums)
print(res)


# another optimized code for min value
def find_min(index,nums):
    if index == len(nums)-1:
        return nums[index]
    min= find_min(index+1,nums)    
    return nums[index] if nums[index]< min else min
    

nums = [2,5,7,3,1]
res = find_min(0,nums)
print(res)



# another optimized code for min value
def find_min(index,nums):
    if index == len(nums)-1:
        return nums[index],nums[index]
    min,max= find_min(index+1,nums)    
    min_val = nums[index] if nums[index]< min else min
    max_val = nums[index] if nums[index]> max else max
    return min_val,max_val
nums = [2,5,7,3,1]
min,max = find_min(0,nums)
print(min)
print(max)



def sum_of_int(n):
    if n == 0:
        return 0
    if n<10:
        return n
    return n%10 + sum_of_int(n//10)
n =12345
res = sum_of_int(n)
print(res)




def count_digit(n):
    if n <9:
        return 1
    return 1 + count_digit(n//10)
n = 123456
res = count_digit(n)
print(res)




#checking the llist is sorted
def check_sorted(index,nums):
    if index == len(nums)-1:
        return True
    next_index = check_sorted(index+1,nums)
    return True if nums[index]< nums[index+1] and next_index else False
nums = [2,4,6,9,89]
res = check_sorted(0,nums)
print(res)
"""




def Tower_of_hanoi(n,source,temp,dest):






Tower_of_hanoi(1,"A","B","C")






































