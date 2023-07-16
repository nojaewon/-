import sys
from collections import deque
input = sys.stdin.readline

N, W, L = map(int, input().split())

waiting = deque(map(int, input().split()))
crossing = deque([0] * W)
time = 0

while waiting:
    next = waiting.popleft()

    if sum(crossing) + next > L:
        while crossing and sum(crossing) + next > L:
            crossing.popleft()
            crossing.append(0)
            time += 1
        crossing[W-1] = next
    else:
        crossing.popleft()
        crossing.append(next)
        time += 1


while crossing:
    crossing.popleft()
    time += 1

print(time)

