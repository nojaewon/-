import sys
from collections import Counter

input = sys.stdin.readline

arr = [0] * 100001

n = int(input())
temp = list(map(int, input().split()))

for i in temp:
    arr[i] += 1

total = 0
for i in range(1, 100000):
    total += arr[i] // i
    arr[i+1] += arr[i] % i

total += arr[100000] // 100000

print(total)