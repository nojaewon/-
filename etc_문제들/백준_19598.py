import sys
import heapq
input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort()

hq = [meetings[0][1]]
for meeting in meetings[1:]:
    if meeting[0] < hq[0]:
        heapq.heappush(hq, meeting[1])
    
    else:
        heapq.heapreplace(hq, meeting[1])

print(len(hq))