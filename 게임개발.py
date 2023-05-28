import sys

def rotate4(d):
    return (d+1)%4



arr = []

n, m = map(int, sys.stdin.readline().rstrip().split())
a, b, d = map(int, sys.stdin.readline().rstrip().split())
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

visited = [[0]*m for _ in range(n)]
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

visited[a][b] = 1
count = 1
d = 0
turn_time = 0

while True:
    d = rotate4(d)
    turn_time += 1
    y = a + direction[d][0]
    x = b + direction[d][1]
    
    # 가보지 않은 칸이 존재한다면 + 그곳이 육지라면; 그 방향으로 한칸
    if visited[y][x] == 0 and arr[y][x] == 0:
        visited[y][x] = 1
        a, b = y, x
        count += 1
        turn_time = 0

    # 네 방향 모두 이미 가본 칸 OR 바다로 되어 있는 칸; 바라보는 칸 유지한채로 뒤로 한칸
    elif turn_time == 4:
        pass
        # 이 때 뒤쪽 방향이 바다인 경우 종료
        y = a - direction[d][0]
        x = b - direction[d][1]
        if arr[y][x] == 1:
            break
        else:
            a, b = y, x
            turn_time = 0

print(count) 