arr = [4,1,5,2,3]
n = len(arr)

for i in range(n):
    curr = arr[i]
    prev = i-1
    while prev >=0 and arr[prev]> curr:
        arr[prev + 1] = arr[prev]
        prev -= 1
    arr[prev + 1] = curr


print(arr)