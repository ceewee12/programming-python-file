def linear_serach(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        return -1

arr =[10,15,20,5,30] 
target = 30

result = linear_serach(arr,target)
print(result)
if result != -1:
    print("element found at index",result)

else:
    print("element not found")