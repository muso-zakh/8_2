# n = int(input())
# arr = []
# x = []

# for _ in range(n):
#     a, b = map(int, input().split())
#     arr.append((a, b))
# arr2 = arr.copy()

# for i in range(len(arr)):
#     x.append(arr[i][0] / arr[i][1])

# y = sorted(x)
# b = 0
# print(y)
# for i in range(len(y)):
#     a = x.index(y[i])
#     print(a)
#     arr[b] = arr2[a]
#     print(arr)
#     print(arr2[a])
#     b += 1

# print(arr)


""""""


n = int(input())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x: x[0] / x[1])

for a, b in arr:
    print(a, b)

