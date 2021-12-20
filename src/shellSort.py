def shellSort(array):
    result = array
    long = len(result)
    interv = long // 2
    while interv > 0:
        for i in range(interv, long):
            temp = result[i]
            j = i
            while j >= interv and result[j - interv] > temp:
                result[j] = result[j - interv]
                j -= interv

            result[j] = temp
        interv //= 2
    return result
