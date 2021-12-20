def bubbleSort(arr):
  n = len(array)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        aux = arr[j]
        arr[j] = arr[j + 1]
        arr[j+1] = aux
