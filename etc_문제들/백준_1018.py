import sys, copy
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
type = ['W', 'B']
for i in range(n):
    arr.append(list(input().rstrip()))

result = 64

def get_count(s, i, j):
    count = 0
    for ii in range(i, i+8):
        ss = copy.deepcopy(s)
        for jj in range(j, j+8):
            if arr[ii][jj] != type[ss]:
                count += 1
            ss = (ss+1) % 2
        s = (s+1) % 2
    return count

for i in range(n-7):
    for j in range(m-7):
        count = min(get_count(0, i, j), get_count(1, i, j))
        result = min(result, count)

print(result)