import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def solution(n, m):
    count = 0
    A, B = [], []

    for i in range(n):
        row = list(map(int, list(input().rstrip())))
        A.append(row)

    for i in range(n):
        row = list(map(int, list(input().rstrip())))
        B.append(row)

    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                if i+2 >= n or j+2 >= m:
                    return -1
                
                count += 1
                for p in range(3):
                    for q in range(3):
                        A[i+p][j+q] = (A[i+p][j+q] + 1) % 2
    return count

print(solution(N, M))
    