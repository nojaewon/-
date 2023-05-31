import sys
input = sys.stdin.readline

numbers = list(map(int, list(input().rstrip())))
count = 0

start = numbers[0]
target = 1 if start == 0 else 0 
# start가 0인 경우 1의 집합 개수를 구함
# start가 1인 경우 0의 집합 개수를 구함
for i in numbers:
    if i == target:
        if i != start:
            count += 1

        target = (target+1) % 2
print(count)

