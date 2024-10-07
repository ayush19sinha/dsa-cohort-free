def mergeSort(arr, start, end):
    if start >= end:
        return
    else:
        mid = (start + end) // 2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid + 1, end)
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    temp = []
    left = start
    right = mid + 1


    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

   
    while left <= mid:
        temp.append(arr[left])
        left += 1

    
    while right <= end:
        temp.append(arr[right])
        right += 1

   
    for i in range(start, end + 1):
        arr[i] = temp[i - start]



arr = [1, 4, 6, 23, 424, 465, 23, 12, 42, 32, 0, 1, 2]
mergeSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
