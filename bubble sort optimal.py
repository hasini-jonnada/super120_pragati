l =[7,2,4,1,0,5]
n = len(l)
for i in range(0,n-1):
    swap =False
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
            swap = True
    if swap == False:
        break
print(l)
