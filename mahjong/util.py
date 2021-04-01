def find_earliest_nonzero_index(arr, index=0):
    while index < len(arr) and arr[index] == 0:
        index += 1
    return index


def modify_list(arr, indices, val):
    for index in indices:
        arr[index] += val
