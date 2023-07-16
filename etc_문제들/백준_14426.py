import sys
input = sys.stdin.readline

n, m = map(int, input().split())

words = []

for i in range(n):
    words.append(input().rstrip())

words.sort()
count = 0
for i in range(m):
    prefix = input().rstrip()
    length = len(prefix)

    start, end = 0, n-1

    while start < end:
        mid = (start+end) // 2

        if prefix > words[mid][:length]:
            start = mid + 1
        else:
            end = mid
    
    if words[start][:length] == prefix:
        count += 1

print(count)



