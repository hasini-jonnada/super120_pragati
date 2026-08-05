import heapq

"""
arr = [9,5,6,19,28,15]
heapq.heapify(arr)
print(arr)
heapq.heappush(arr,2)
print(arr)
print(heapq.heappop(arr))
print(arr)
print(heapq.nlargest(3,arr))
"""



arr = [9,5,6,19,28,15]
arr = [-i for i in arr]
heapq.heapify(arr)
print(arr)

heapq.heappush(arr,-2)
print(arr)
print(-heapq.heappop(arr))
print(arr)
print(heapq.nlargest(3,arr))
