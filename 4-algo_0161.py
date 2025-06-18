arr = ['A', 'S', 'S', 'A', 'L', 'O', 'M']

n = int(input())
arr2 = list(input().split())
i = 0

while arr:
    if arr2.count(arr[i]) == 0:
        print('NO')
        break
    arr.remove(arr[i])

else:
    print('YES')
