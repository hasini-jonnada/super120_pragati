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


