import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 입력 예시
# 5 8 3
# 2 4 5 4 6

# 가장 큰 수 * ((m // (k+1))*k + m%(k+1) // k)
# 2번째 큰 수 * (m // (k+1))

arr.sort(reverse=True)
print(arr[0] *((m // (k+1))*k + m%(k+1) // k) + arr[1] * (m // (k+1)) )
