import sys
input = sys.stdin.readline

def combination(arr, r):
    result = []
    def generate(chosen):
        if len(chosen) == r:
            result.append(chosen[:])
            return
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])
    return result

a = []
b = []
N, M = map(int, input().split())

for i in range(N):
    p = list(map(int, input().split()))

    for j in range(N):
        if p[j] == 1:
            a.append((i, j))
        elif p[j] == 2:
            b.append((i, j))

# M개의 조합 중 집과 각각 치킨집의 최솟값의 합의 최솟값을 구해야한다.
min_city_chicken = int(1e9)
b = combination(b, M)

# 조합들을 순회 x는 배열
for x in b:
    total = 0
    # 집 순회
    for y in a:
        chicken_dist = (N-1) * 2
        # 치킨집 순회하면서 치킨 거리 구하기
        for z in x:
            chicken_dist = min(chicken_dist, abs(y[0] - z[0]) + abs(y[1] - z[1]))
        
        total += chicken_dist

    # 도시의 치킨 거리 구하기
    min_city_chicken = min(min_city_chicken, total)

print(min_city_chicken)



    
    