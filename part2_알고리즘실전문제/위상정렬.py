from collections import deque

v, e = map(int, input().split())

# 진입차수(indegree)는 0으로 초기화
indegree = [0] * (v+1)

# 그래프 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입차수를 1증가
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=' ')

topology_sort()
        