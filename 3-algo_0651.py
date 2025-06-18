a = int(input())
arr = list(input().split())

n = len(arr)
x = 0

for j in range(len(arr)):
    for i in range(n-1):
        min = i
        
        if arr[i+1] < arr[min]:
            x += 1
            arr[i+1], arr[min] = arr[min], arr[i+1]
         
print(x)