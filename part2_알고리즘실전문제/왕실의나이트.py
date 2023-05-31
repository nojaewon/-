# 8 x 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 이동할 수 있는 경우의 수

pos = input()
move = [(-2, -1), (-1, -2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
row = ord(pos[0]) - ord('a')
col = int(pos[1])
count = 0

for k in move:
    if (0 <= row + k[0] and row + k[0] < 8) and (0 <= col + k[1] and col + k[1] < 8):
        count += 1

print(count)
 
