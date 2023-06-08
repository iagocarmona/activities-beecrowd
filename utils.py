def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def printArray(arr):
    idx = 0
    for i in arr:
        if idx < len(arr) - 1:
            print(i, end = ' ')
        else:
            print(i)
        idx = idx + 1