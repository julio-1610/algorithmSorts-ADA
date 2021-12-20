from datetime import datetime
from random import randrange


from shellSort import shellSort
from bubbleSort import bubbleSort
from insertionSort import insertionSort
from mergeSort import doMergeSort
from quickSort import quickSort

sizes = [100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000]

for s in sizes:
    vect = []
    for i in range(s):
        vect.append(randrange(s*2))

    print(f"Tamaño del vector: {s}")
    init_time = datetime.now()
    respuesta = bubbleSort(vect)
    end_time = datetime.now()
    print('\tDuración Bubble Sort: \t\t{}'.format(end_time - init_time))
    init_time = datetime.now()
    respuesta = insertionSort(vect)
    end_time = datetime.now()
    print('\tDuración Insertion Sort: \t{}'.format(end_time - init_time))
    init_time = datetime.now()
    respuesta = doMergeSort(vect)
    end_time = datetime.now()
    print('\tDuración Merge Sort: \t\t{}'.format(end_time - init_time))
    init_time = datetime.now()
    respuesta = quickSort(vect, 0, s-1)
    end_time = datetime.now()
    print('\tDuración Quick Sort: \t\t{}'.format(end_time - init_time))
    init_time = datetime.now()
    respuesta = shellSort(vect)
    end_time = datetime.now()
    print('\tDuración Shell Sort: \t\t{}'.format(end_time - init_time))
