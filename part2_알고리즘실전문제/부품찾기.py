def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        
    return None

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))


arr.sort()

for i in arr2:
    result = binary_search(arr, i, 0, n-1)
    if result != None:
        print('yes', end=" ")
    else:
        print('no', end=" ")