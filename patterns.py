"""c = 4
for i in range(c):
    for j in range(c - i):
        print(" ",end = " ")
    for k in range(4):
        print("*",end = " ")
    print()
    
c = 4
r = 1
for i in range(c):
    for j in range(r + i):
        print(" ",end = " ")
    for k in range(3):
        print("*",end = " ")
    print()
    
c = 4
r = 1
for i in range(c):
    for j in range(c - i-1):
        print(" ",end = " ")
    for k in range(r + (2*i)):
        print("*",end = " ")
    print()
    
c = 4
r1 = 1
r = 7
for i in range(c):
    for j in range(r1 + i-1):
        print(" ",end = " ")
    for k in range(r - (2*i)):
        print("*",end = " ")
    print()
    

c = 6
r = 1
for i in range(c):
    for j in range(c-i):
       print(" ",end = " ")
    print("*",end = " ")
    if i != 0 and i != c - 1:
        for L in range(r+(2*(i-1))):
            print(" ",end = " ")
    if i == c-1:
        for j in range(r+(2*(i-1))):
            print("*",end = " ")
    if i != 0:
        print("*")
    print()
    
    
c = 14
r = 0
r1 = (c*2)-1
for i in range(c):
    for j in range(r+i):
      print(" ",end = " ")
    print("*",end = " ")
    if i == 0:
        for k in range(r1-2):
            print("*",end = " ")
    if i != 0 and i!= c-1:
        for L in range((r1-4)- (2*(i-1))):
            print(" ",end = " ")
    if i != c-1:
        print("*")
    print()
    





c = 6
r = 1
for i in range(c):
    for j in range(c-i-1):
       print(" ",end = " ")
    if i != c-1:
        print("*",end = " ")
    if i != 0 and i != c - 1:
        for L in range(r+(2*(i-1))):
            print(" ",end = " ")
    #if i == c-1:
     #   for j in range(r+(2*(i-1))):
      #      print("*",end = " ")
    if i != 0 and i != c-1:
        print("*",end = " ")
    if i != 5:
        print()
    if i != 5:
        print()
    
c = 6
r = 0
r1 = (c*2)-1
for i in range(c):
    for j in range(r+i):
      print(" ",end = " ")
    print("*",end = " ")
    if i == 0:
        for k in range(r1-2):
            print("*",end = " ")
    if i != 0 and i!= c-1:
        for L in range((r1-4)- (2*(i-1))):
            print(" ",end = " ")
    if i != c-1:
        print("*",end = " ")
    print()
    print()



n = 5
for i in range(5):
    for j in range(n-i-1):
        print(" ",end = " ")
    for k in range(i+1,0,-1):
       print(k,end = " ")
    for L in range(i):
        print(L+2,end = " ")
    print()








