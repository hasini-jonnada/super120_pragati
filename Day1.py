
#move even into end of list
a = [1,2,4,5,6]
for i in a[:]:
    if i%2 == 0:
        a.append(i)
        a.remove(i)
        
print(f"ans = {a}")
    



#remmove duplicates
a = [7,8,1,8,9]
res = []

for i in a:
    if i not in res:
        res.append(i)
print(res)
    


#adding primes in a give integer
a = int(input("enter a value:"))
sum = 0
for i in str(a):
    if i in "2357":
        sum += int(i)
print(sum)


#adding each value in an integer
a = int(input("enter a value:"))
while a > 9:
    sum = 0
    a = str(a)
    for i in a:
        sum += int(i)
    a = sum
print(sum)


#STRING ROTATIONS


#right rotation of a string 
s = "abcd"
n = int(input("enter a value :"))
for i in range (n%len(s)):   
    s = s[-1] + s[:-1:]
print(s)


#right rotation of a string 
s = "abcd"
n = int(input("enter a value :"))  
n = n % len(s)
s = s[-n:] + s[:-n]
print(s)




#left rotation of a string 
s = "abcd"
n = int(input("enter a value :"))
for i in range (n%len(s)):   
    s = s[1:] + s[0]
print(s)



#left rotation of a string 
s = "abcd"
n = int(input("enter a value: "))
n = n % len(s)  # normalize
s = s[n:] + s[:n]
print(s)



a = [1,4,2,6,7,8]
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        print(False)
        break;
       
else:
    print(True)
        


#checking prime or not
a = int(input("enter a value:"))
count = 0
for i in range(2, a):
    if a%i ==0:
        count += 1
if count == 2:
    print("not a prime")
else:
    print("prime numnber")














