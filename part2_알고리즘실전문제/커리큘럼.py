import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
time = [0] * (n+1)
graph = [[0] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
que = deque()

for i in range(1, n+1):
    value = list(map(int, input().split()))
    graph[i][0] = value[0]
    time[i] = value[0]

    for j in range(1, len(value)-1):
        graph[value[j]].append(i)
        indegree[i] += 1


for i in range(1, n+1):
    if indegree[i] == 0:
        que.append(i)

while(que):
    now = que.popleft()
    for x in range(1, len(graph[now])):
        target = graph[now][x]

        indegree[target] -= 1
        graph[target][0] = max(graph[target][0], graph[now][0] + time[target])

        if indegree[target] == 0:
            que.append(target)

for i in range(1, n+1):
    print(graph[i][0])
    

    