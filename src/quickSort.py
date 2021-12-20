def division(arr, l, h):
    i = (l-1)         
    pivot = arr[h]     
 
    for j in range(l, h):
 
        if arr[j] <= pivot:
 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
 
def quickSort(array, l, h):
    arr = array
    if len(arr) == 1:
        return arr
    if l < h:
        
    
        pi = division(arr, l, h)
        result = []
        result.append(quickSort(arr, l, pi-1))
        result.append(quickSort(arr, pi+1, high))
    return arr
 
