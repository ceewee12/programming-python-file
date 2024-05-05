# a= 5
# b=2
# print(a//b)
# print(a%b)
# print(a/b)
# print(a|b)
# print(a>>b)
# age = 25
# is_student  = False
# if age < 18:
#     print('you ARE minor')
# elif age >= 18 or is_student:
#     print('u r student')
# else:
#     print('u r adult')

# x = 6
# y = 4
# if x > 5:
#     if y>5:
#         if x+y > 15:
#             print('u r right')
#         else:
#             print('opps sorry') 
#     else:
#         print('u r wrong')
# else:
#     print('false')
# no = [1,20,40,30,50]
# no1 =  200 in no
# print(no1)

# def linear_search(arr, target):
#     # The triple quote is a python string to specify what a function does
#     """
#     Performs a linear search on the given list 'arr' to find the 'target' element.
#     Returns the index of the target element if found, otherwise returns -1.
#     """
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i # Return the index of the target element: 
#             # Just like break statement, return statement will immediately exit the function itself
#     return -1

# # Usage of linear search
# my_list = [5, 2, 9, 1, 7]
# target = 9

# index = linear_search(my_list, target)
# if index == -1:
#     print(f"Target {target} not found in the list")
# else:
#     print(f"Target {target} found at index {index}")
# def insertion_sort(arr):
#     """
#     Sorts the given list 'arr' in ascending order using the insertion sort algorithm.
#     """
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1

#         # Shift elements greater than 'key' to the right
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1

#         # Insert 'key' at the correct position
#         arr[j + 1] = key

#     return arr

# my_list = [5, 2, 9, 1, 7]

# sorted_list = insertion_sort(my_list)
# print("Sorted list:", sorted_list)

# # Output: Sorted list: [1, 2, 5, 7, 9]
a = [2,3,5,6,4,7]

