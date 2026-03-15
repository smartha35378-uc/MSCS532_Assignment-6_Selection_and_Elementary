
def partition(arr, pivot):
    lows = []
    highs = []
    pivots = []

    for el in arr:
        if el < pivot:
            lows.append(el)
        elif el > pivot:
            highs.append(el)
        else:
            pivots.append(el)

    return lows, pivots, highs


def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]

    pivot = median_of_medians(medians, len(medians)//2)

    lows, pivots, highs = partition(arr, pivot)

    if k < len(lows):
        return median_of_medians(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))
