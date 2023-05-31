import sys
input = sys.stdin.readline

numbers = list(map(int, list(input().rstrip())))
result = numbers[0]

# 두 수 중에서 하나라도 1이하면 더하기 2이상이면 곱하기가 더 크다.
for i in range(1, len(numbers)):
    if result <= 1 or numbers[i] <=1:
        result += numbers[i]
    else:
        result *= numbers[i]

print(result)

