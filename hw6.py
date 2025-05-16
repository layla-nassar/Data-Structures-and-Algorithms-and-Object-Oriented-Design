def bubble_sort(arr):
    def bubble_recursive(arr, n, swaps):
        if n == 1:
            return arr, swaps
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
        return bubble_recursive(arr, n - 1, swaps)

    return bubble_recursive(arr, len(arr), 0)


def selection_sort(arr):
    def selection_recursive(arr, i, swaps):
        if i == len(arr):
            return arr, swaps
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
        return selection_recursive(arr, i + 1, swaps)

    return selection_recursive(arr, 0, 0)


def insertion_sort(arr):
    def insertion_recursive(arr, i, swaps):
        if i <= 0:
            return arr, swaps
        if arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            swaps += 1
        return insertion_recursive(arr, i - 1, swaps)

    for i in range(1, len(arr)):
        arr, _ = insertion_recursive(arr, i, 0)
    return arr, _