N = int(input())
A = list(map(int,list(input())))
B = list(map(int, list(input())))

def count(A, B):
    res = 0
    a = A[:]
    for i in range(1, N):
        if a[i-1] == B[i-1]:
            continue
        
        res += 1
        for j in range(i-1, i+2):
            if j < N:
                a[j] ^= 1
    
    if a == B:
        return res
    else:
        return 1e9

res1 = count(A, B)

A[0] ^= 1
A[1] ^= 1

res2 = count(A, B) + 1

result = min(res1, res2)
if result == 1e9:
    print(-1)
else:
    print(result)

    

            




