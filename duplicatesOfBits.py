#unique number
a = [2,3,4,3,4,9,2,5,5]
res = a[0]
for i in range(1,len(a)):
    res = res^a[i]
print(res)




#ascii values
a = "gnfjfd"
sum =0
for i in range (len(a)):
    ascii_val = ord(a[i])
    sum = sum + ascii_val
print(sum)
print(ord('A'))


    
#assigning 1,2,3... for a,b,c...
a = "abcde"
sum =0
for i in range (len(a)):
    val = (ord(a[i])-96)
    sum = sum + val
print(sum)




#convert the lower case to upper case A= 65, a = 97
a = "aBCdeF"
res = ""
for i in a:
    if ord(i)>96:
        res += chr((ord(i)-32))
    else:
        res += chr((ord(i)+32))
print(res)

















































