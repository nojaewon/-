import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())
for t in range(T):
    que = deque()
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    cost = [0 for _ in range(n+1)]

    for i in range(k):
        a, b = map(int, input().split())
        indegree[b] += 1
        graph[a].append(b)

    w = int(input().rstrip())

    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)
            cost[i] += arr[i-1]
    
    while que:
        now = que.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            cost[i] = max(cost[i], cost[now] + arr[i-1])

            if indegree[i] == 0:
                que.append(i)
    
    print(cost[w])