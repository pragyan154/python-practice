# import snoop
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1], arr[j]

#     return arr

# arr=[2,34,1,33,6]
# print(bubble_sort(arr))

#used swapped
# @snoop
# def bubble_sort(arr):
#     n = len(arr)
#     swapped = True
    
#     while swapped:
#         swapped = False
#         for j in range(0,n-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1], arr[j]
#                 swapped = True

#     return arr

# arr=[2,34,1,33,6,1]
# print(bubble_sort(arr))

#--------------------------------------------------merge sort

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = mergesort(left)
    right_sorted = mergesort(right)

    i=j=0

    result = []
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            result.append(left_sorted[i])
            i += 1

        else:
            result.append(right_sorted[j])
            j += 1

    result += left_sorted[i:]
    result += right_sorted[j:]

    return result

arr = [33,1,2,44,12,4]
print(mergesort(arr))