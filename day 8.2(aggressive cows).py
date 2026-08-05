"""def checker(max_cap,books,student):
    cur_student ,cur_capacity= 1,books[0]
    for book in books[:]:
        if book + cur_capacity > max_cap:
            cur_student +=1
            cur_capacity = book
            if cur_student > student:
                return False
        else:
            cur_capacity+= book
    return True
def allocate_books(books,student):
    n= len(books)
    if n<student:
        return -1
    min,max = books[-1],sum(books)
    
    l = min
    r = max
    ans = max
    while l<=r:
        mid = (l+r)//2
        if checker(mid,books,student):
            ans = mid
            r=mid-1
        else:
            l= mid+1
    return ans
books = [12,34,67,90]
res = allocate_books(books,2)
print(res)
"""


def checker(max_distance,house,cows):
    cow = 1
    last_cow = house[0]
    for distance in house[1:]:
        if distance - last_cow >= max_distance:
            cow+=1
            last_cow = distance
            if cow >= cows:
                return True
    return False
        

def aggressive_cows(house,cows):
    house.sort()
    min = 0
    max = house[-1] - house[0]
    
    l= min
    r= max
    ans = 0
    while l<=r:
        mid = (l+r)//2
        if checker(mid,house,cows):
            ans = mid
            l =mid+1
        else:
            r=mid-1
    return ans

            
house = [10,1,2,7,5]
res = aggressive_cows(house,3)
print(res)



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r
        while l<r:
            mid = (l+r)//2
            hour =0
            for banana in piles:
                hour += math.ceil(banana/mid)
            if hour<=h:
                ans = hour
                l = mid+1
            else :
                r = mid+1
        return ans
        
    
    














