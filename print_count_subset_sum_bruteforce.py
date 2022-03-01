from functools import reduce
def findSubset(arr, target):
    sum = 0
    for i in range(len(arr)):   
        sum = arr[i]     
        for j in range(i+1, len(arr)):
            if target-sum-arr[j] == 0:                
                return [arr[i], arr[j]]    
    return False

arr = [2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6, 2, 3, 7, 6]
target = 12
# print(findSubset(arr, targeot))
print(reduce(lambda x,y: x+y, arr))

arr1 = [[1,2,4],[6,7,3]]

for i in range(len(arr1)):
    arr1[i] = sorted(arr1[i])
print(arr1)