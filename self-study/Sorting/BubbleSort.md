### Bubble Sort: 

``` python

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


arr1 = [1, 52, 7, 2, 15, 13, 34, 45, 11, 24]
ans = bubbleSort(arr1)
print(ans)
