def bubble_sort(arr):
    """
    this func return sorted array or list using bubble sort method
    :param arr: array or list
    :return: sorted array or list
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


example_lst = [3, 5, 73, 6, 7, 4, 3, 3, 6, 7, 7]
print(bubble_sort(example_lst))
