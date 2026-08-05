#monotonic increasing stack
a = [4,5,6,1,2,4,3]
stack =[]
for val in a:
    while stack and stack[-1]> val:
        stack.pop()
    stack.append(val)
print(stack)



#monotoni decreasing stack
a = [4,5,6,1,2,4,3]
stack =[]
for val in a:
    while stack and stack[-1]< val:
        stack.pop()
    stack.append(val)
print(stack)

#next greater
a = [4,5,6,1,2,4,3]
stack =[]
res = [-1]*len(a)
for i,val in enumerate(a):
    while stack and a[stack[-1]]< val:
        index = stack.pop()
        res[index] = val
    stack.append(i)
print(res)
