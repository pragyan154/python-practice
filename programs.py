import sys
script_name = sys.argv[0]
arg1 = sys.argv[1]
arg2 = sys.argv[2]
sys.path.append("contacts")
print(arg1,arg2,script_name)















# n = 2048
# outc = 0
# inc = 0
# while n > 1:
#     outc += 1
#     j = 0
#     while j < n :
#         inc += 1
#         j += 1
#     n = n//2

# print(outc,inc)

#O(n2) programs
#print pairs
# arr = [1, 2, 3, 4]
# n = len(arr)
# for i in range(n):
#     for j in range(i+1, n):
#         print(arr[i], arr[j])
# #---------------------------------------------


# # maximum difference between two number in array 
# def max_difference(arr):
#     n = len(arr)
#     max_diff = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             diff = abs(arr[i] - arr[j])
#             if diff > max_diff:
#                 max_diff = diff
#     return max_diff
# #--------------------------------------------------


# arr = [7, 2, 9, 5, 1, 3, 8]
# print(max_difference(arr))

# def subarray_sum(arr, start, end):
#     sa_sum = sum(arr[start:end+1])
#     return sa_sum

# print(subarray_sum(arr,2,5))

# # using prefix sum
# def calculate_prefix_sum(arr):
#     n = len(arr)
#     for i in range(1, n):
#         arr[i] += arr[i - 1]
#     return arr

# a = calculate_prefix_sum(arr)
# print(a)
# print(a[5]-a[1])


# def reverse_array(arr,start,end):

#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1

# arr = [1, 2, 3, 4, 5]


# def rotate_array(arr, n):

#     rotations = n % len(arr)
    
#     #reversed the entire array
#     reverse_array(arr, 0, len(arr) - 1)

#     #reverse the first part upto rotation
#     reverse_array(arr, 0, rotations - 1)

#     # reverse remaining part
#     reverse_array(arr, rotations, len(arr) - 1)

#     return arr

# print(rotate_array(arr,4))

# def second_largest(arr):
#     largest = arr[0]
#     # assigned first element as largest
#     second_l = float('-inf')
#     # to comapre , assigned second L as None
#     for i in arr[1:]:
#         if i > largest:
#             second_l = largest
#             largest = i
#         elif second_l is None or i > second_l:
#             second_l = i

#     return second_l

# arr = [-4,-5,-1,2]
# # print(second_largest(arr))




# first = max(arr[0], arr[1])
# second = min(arr[0], arr[1])

# for i in range(1, len(arr)):
#     if arr[i] > first:
#         second = first
#         first = arr[i]
#     elif arr[i] > second and arr[i] != first:
#         second = arr[i]

# print(second)

# # Example usage

# a = [1,2,3,4,4,5,6,7]
# ranges = [[1,2],[1,5],[2,6]]
# evens = [0]*len(a)
# def get_evens(arr):
#     total_even = 0
#     for i in range(len(arr)) :
#         if arr[i] % 2 == 0 :
#             total_even += 1
#         evens[i] = total_even



# get_evens(a)
# for sarr in (ranges):
#     start , end = sarr[0], sarr[1]
#     no_of_evns = evens[end+1]-evens[start]
#     print("start: " , start, "end: ", end, "->" , no_of_evns)

