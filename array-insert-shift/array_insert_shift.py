def insertShiftArray(arr, val):
  
    n = len(arr)
    mid = (n // 2) + (n % 2)
    shifted = [None] * (n+1)

    for i in range(mid):
        shifted[i] = arr[i]
    shifted[mid] = val

    for i in range(mid, n):
        shifted[i+1] = arr[i]

    return shifted   


ex1 = insertShiftArray([2,4,6,-8], 5)
ex2 = insertShiftArray([42,8,15,23,42], 16)   


print(ex1)
print(ex2)