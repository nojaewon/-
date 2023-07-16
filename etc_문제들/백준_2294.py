import sys
input = sys.stdin.readline

n, k = map(int, input().split())

p = [k+1 for _ in range(100001)]
for _ in range(n):
    p[int(input().rstrip())] = 1

for i in range(1, k+1):
    for j in range(1, k+1):
        if i + j <= k:
            p[i + j] = min(p[i] + p[j], p[i + j])

if p[k] == k+1:
    print(-1)
else:
    print(p[k])