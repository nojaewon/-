import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]
distance = [INF] * (n+1)
visited = [False] * (n+1)

def get_shortest_node():
    min_value = INF
    index = 1
    for i in range(1, n+1):
        if min_value > distance[i] and not visited[i]:
            min_value = distance[i]
            index = i
    return index

for _ in range(m):
    i, j, k = map(int, input().split())
    graph[i][j] = k

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(1, n+1):
    distance[i] = graph[c][i]

visited[c] = True

for _ in range(n-1):
    next = get_shortest_node()
    visited[next] = True

    for i in range(1, n+1):
        if not visited[i] and (distance[i] > graph[c][next] + graph[next][i]):
            distance[i] = graph[c][next] + graph[next][i]

max_value = 0
count = 0
for i in range(1, n+1):
    if distance[i] < INF:
        count += 1

        max_value = max(distance[i], max_value)

print(count-1, max_value)