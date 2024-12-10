def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        result.append(left[i] if left[i] <= right[j] else right[j])
        i, j = (i + 1, j) if left[i] <= right[j] else (i, j + 1)
    return result + left[i:] + right[j:]

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted Array:", merge_sort(arr))
