# Python file to store all the algorithms which will be displayed and all the helped functions needed to make them works

# Helpers
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def heapify(array, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


# Compares adjacent elements and swaps them until they are in the correct order]
def bubbleSort(array):
    if (len(array) == 1):
        return
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if (array[j] > array[j + 1]):
                swap(array, j, j + 1)
                yield array


# assigns first element as minimum and compares it to all elements until it reaches an element bigger than it
# then assigns the next element in the front of the array as the minimum until everything is sorted
def selectionSort(array):
    for x in range(len(array)):
        min = x
        for i in range(x + 1, len(array)):
            # select the minimum element in each loop
            if array[i] < array[min]:
                min = i
                yield array
        # put min at the correct position
        (array[x], array[min]) = (array[min], array[x])
        yield array


# traverses through array and each time an element encounters another element bigger than it shifts the bigger element
# one position upwards
def insertionSort(array):
    # Traverse through 1 to len(arr)
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            yield array
        array[j + 1] = key


def bucketSort(array, n):
    bucket = []
    # Initialize empty buckets for the amount of elements in the array
    for i in range(len(array)):
        bucket.append([])
    # Insert elements from the unsorted array into the buckets
    for j in array:
        index_b = int(j / n)
        if (index_b <= n):
            bucket[index_b].append(j)
        else:
            bucket[len(array) - 1].append(j)
    # Sort
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
            yield array


def heapSort(array):
    n = len(array)
    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        # Swap
        array[i], array[0] = array[0], array[i]
        # Heapify root element
        heapify(array, i, 0)
        yield array


# Simplified version of insertion sort, where elements that are far apart are
# sorted until the interval between smaller elements becomes smaller
def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
                yield array
            array[j] = temp
        interval //= 2
        yield array


def quickSort(array, low, high):
    if (low < high):
        pivot = low
        i = low
        j = high
        while (i < j):
            while array[i] <= array[pivot] and i < high:
                i += 1
            while array[j] > array[pivot]:
                j -= 1
            if (i < j):
                array[i], array[j] = array[j], array[i]
                yield array
        array[pivot], array[j] = array[j], array[pivot]
        yield from quickSort(array, low, j - 1)
        yield from quickSort(array, j + 1, high)
    else:
        yield array
