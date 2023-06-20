import sys

input = sys.stdin.readline

def my_solution():
    n = list(map(int, list(input().rstrip())))
    l = len(n)//2

    if sum(n[:l]) == sum(n[l:]):
        print("LUCKY")
    else:
        print("READY")

my_solution()
    

