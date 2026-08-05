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


def sqrt(n):
    l=1
    r=n
    while l<=r:
        mid =(l+r)//2
        if mid * mid >= n:
            ans = mid
            r=mid-1
        elif mid*mid < n:
            l= mid+1
    return ans
            
res = sqrt(25)
print(res)





















