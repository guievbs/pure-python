def search(arr) -> int:
    low = arr[0]
    low_index = 0

    for i in range(1, len(arr)):
        if arr[i] < low:
            low = arr[i]
            low_index = i

    return low_index


def selection_sort(arr) -> list:
    new_arr = []

    for i in range(len(arr)):
        low = search(arr=arr)
        new_arr.append(arr.pop(low))

    return new_arr


arr = [1, 4, 7, 98, 9, 2, 5, 8]

arr_sort = selection_sort(arr=arr)

print((arr_sort))
