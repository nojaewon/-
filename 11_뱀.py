import sys
from collections import deque
input = sys.stdin.readline

apples = []
rotate = deque()
warm = deque()

k = 0
# 왼쪽 k = (k+3) % 4 , 오른쪽 k = (k+1) % 4
# [오른쪽, 아래, 왼쪽, 윗쪽]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]



# 입력 정보 저장
N = int(input().rstrip())
K = int(input().rstrip())

for _ in range(K):
    y, x = map(int, input().rstrip().split())
    apples.append((y, x))

L = int(input().rstrip())

for _ in range(L):
    time_and_direction = input().rstrip().split()
    rotate.append((int(time_and_direction[0]), time_and_direction[1]))

# 보드 초기화, 0으로 초기화
board = [[0] * (N+1) for _ in range(N+1)]

# 사과 위치시키기, 2로 초기화
for apple in apples:
    y, x = apple
    board[y][x] = 2

# 지렁이 위치
pos_x = 1
pos_y = 1
board[pos_x][pos_y] = 1
warm.append((pos_y, pos_x))

time = 0
next_rotate = rotate.popleft()

while True:
    time += 1
    
    next_y = pos_y + dy[k]
    next_x = pos_x + dx[k]

    if next_y > 0 and next_y < N+1 and next_x > 0 and next_x < N+1:
        if board[next_y][next_x] == 0:
            # 지렁이가 지나갈 수 있을때
            tail = warm.popleft()
            warm.append((next_y, next_x))
            board[next_y][next_x] = 1
            board[tail[0]][tail[1]] = 0
            pos_y, pos_x = next_y, next_x


        elif board[next_y][next_x] == 1:
            break
            # 지렁이가 자기 몸에 부딪혔을때
        else:
            # 2일때 즉 사과를 만났을 때
            board[next_y][next_x] = 1
            warm.append((next_y, next_x))
            pos_y, pos_x = next_y, next_x

        
        if time == next_rotate[0]:
            if next_rotate[1] == 'L':
                k = (k + 3) % 4
            elif next_rotate[1] == 'D':
                k = (k + 1) % 4

            if rotate:
                next_rotate = rotate.popleft()
    else:
        break

print(time)