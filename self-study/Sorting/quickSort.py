def quickSort(arr, low, high):
    if low < high:
        pivotIndex = partition(arr, low, high)  
        quickSort(arr, low, pivotIndex - 1)     
        quickSort(arr, pivotIndex + 1, high)    

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:  
            i += 1
        while i <= j and arr[j] > pivot:   
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]  
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]  
    return j  
    
arr = [1,32,242,365,123,25,1,2,22,23,432,1123,0,7,-1,3]
quickSort(arr, 0 , len(arr)-1)
print(arr)
