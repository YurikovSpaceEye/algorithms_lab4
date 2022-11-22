def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array


def comb_sort(array):
    n = len(array)
    step = n
    swaps = True
    while step > 1 or swaps:
        step = max(1, int(step / 1.25))
        swaps = False
        for i in range(n - step):
            j = i+step
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swaps = True
