import sys
input = sys.stdin.readline



n, m = map(int, input().split())
parent = [0 for _ in range(n+1)]

# parent table 초기화
for i in range(n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def check(parent, k, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if k == 0:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    else:
        if a == b:
            print('YES')
        else:
            print('NO')
 
for i in range(n+1):
    k, a, b = map(int, input().split())

    check(parent, k, a, b)


