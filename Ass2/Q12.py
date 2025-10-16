from collections import Counter
arr = [1,2,3,2,3,4,4,4,5,4,5,6]
n = len(arr)
mean =0
for i in range(0,n):
    mean += arr[i]
mean /= n
arr.sort()
median = arr[(n+1)//2]
mode =max(Counter(arr).values())
print(mean)
print(median)
print(mode)