#adding 1 to last digit if it is 2 digits add 1 to before num and print 0 at last
a = [9,9,9,9]

for i in range(len(a)-1,-1,-1):
    if a[i]+1 == 10:
        a[i] = 0
    else:
        a[i] += 1;break
else:
    a = [1] + a 
print(a)



#afbrcgD 
a = "abcd"
b = "frg"
i=0
res = ""
while i<len(a) and i<len(b):
    res += a[i]+b[i]
    i+=1
res += a[i:].upper()
res += b[i:].upper()
print(res)
    
