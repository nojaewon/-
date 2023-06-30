import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().rstrip())

numbers = []
tokens_of_number = defaultdict(int)

for _ in range(n):  
    token = input().rstrip()
    token_length = len(token)

    for i in range(token_length):
        tokens_of_number[token[i]] += pow(10, token_length - i - 1)

for token in tokens_of_number.values():
    numbers.append(token)

length = len(numbers)
numbers.sort(reverse=True)
numbers = [numbers[i] * (10 - i - 1) for i in range(length)]

print(sum(numbers))

    





