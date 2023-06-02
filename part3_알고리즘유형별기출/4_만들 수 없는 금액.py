import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
total = 0

arr.sort()

for i in range(n):
    for j in range(total+1, total+arr[i]+1):
        temp = j-arr[i]
        if temp < 0 or temp > total:
            print(j)
            exit(1)
    total += arr[i]
