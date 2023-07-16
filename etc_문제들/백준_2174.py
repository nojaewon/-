import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int , input().split())

arr = [[0]*A for _ in range(B)]
robot = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution():
    for i in range(N):
        temp = input().split()
        x, y, d = int(temp[0]), int(temp[1]), temp[2]
        arr[y-1][x-1] = i+1
        if d == 'N':
            robot.append((y-1, x-1, 0))
        elif d == 'E':
            robot.append((y-1, x-1, 1))
        elif d == 'S':
            robot.append((y-1, x-1, 2))
        else:
            robot.append((y-1, x-1, 3))

    for _ in range(M):
        temp = input().split()
        idx, command, count = int(temp[0]), temp[1], int(temp[2])
        y, x, d = robot[idx-1]

        if command == 'L':
            for _ in range(count):
                d = (d+3) % 4
            robot[idx-1] = (y, x, d)
        elif command == 'R':
            for _ in range(count):
                d = (d+1) % 4
            robot[idx-1] = (y, x, d)
        elif command == 'F':
            for i in range(count):
                ny = dy[d] + y
                nx = dx[d] + x
                if not (0<=ny<B) or not (0<=nx<A):
                    print(f'Robot {idx} crashes into the wall')
                    return
                
                elif arr[ny][nx] != 0:
                    print(f'Robot {idx} crashes into robot {arr[ny][nx]}')
                    return
            
                arr[y][x] = 0
                arr[ny][nx] = idx
                y = ny
                x = nx
                robot[idx-1] = (ny, nx, d)
    print('OK')


solution()