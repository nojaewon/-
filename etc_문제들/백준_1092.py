import sys
import math
input = sys.stdin.readline

n = int(input().rstrip())
p = list(map(int, input().split()))
p.sort(reverse=True)

m = int(input().rstrip())
q = list(map(int, input().split()))
q.sort(reverse=True)

if p[0] < q[0]:
    print(-1)
    sys.exit() 

idx = 0
while 0 < len(q):
    for i in p:
        for j in q:
                if i >= j:
                    q.remove(j)
                    break
    idx += 1

print(idx)



