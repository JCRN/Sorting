import math


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    # TO-DO
    print('array A:', arrA)
    print('array B:', arrB)
    a_idx, b_idx = 0, 0
    while a_idx < len(arrA) and b_idx < len(arrB):
        if arrA[a_idx] < arrB[b_idx]:
            merged_arr.append(arrA[a_idx])
            a_idx += 1
        else:
            merged_arr.append(arrB[b_idx])
            b_idx +=1
    if a_idx == len(arrA):
        merged_arr.extend(arrB[b_idx:])
    else:
        merged_arr.extend(arrA[a_idx:])
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right)


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO
#
#     return arr
#
#
# def merge_sort_in_place(arr, l, r):
#     # TO-DO
#
#     return arr
#
#
# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):
#     return arr
