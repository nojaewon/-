import sys

input = sys.stdin.readline

def my_solution():
    k = list(input().rstrip())
    k.sort()

    j, total  = 0, 0
    for idx, i in enumerate(k):
        if ord(i) >= 65:
            j = idx
            break
        else:
            total += int(i)
    print("".join(k[idx:]), end="")
    print(total)



my_solution()