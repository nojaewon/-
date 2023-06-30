import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
que = deque()
answer = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, 0])


que.append([x, 0])
visited[x] = True
while que:
    now, degree = que.popleft()
    
    for target in graph[now]:
        if not visited[target[0]]:
            que.append(target)
            visited[target[0]] = True
            target[1] = degree + 1
            if degree+1 == k:
                answer.append(target[0])
    
if answer:
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)








    
