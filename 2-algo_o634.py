arr = list(input().split())

n = len(arr)


for j in range(n):
    max = j

    for i in range(j+1, n):
        if arr[i].count('a') > arr[max].count('a'):
            max = i

    arr[j], arr[max] = arr[max], arr[j]
        
print(" ".join(arr))