KEY = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
LOCK = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# def rotate_a_metrix_by_90_degree(a):
#     n = len(a) # 행 길이
#     m = len(a[0]) # 열 길이

#     result = [[0] * n for _ in range(m)]
#     for i in range(n):
#         for j in range(m):
#             result[j][n - i - 1] = a[i][j]
#     return result

# def check(new_lock):
#     lock_length = len(new_lock) // 3
#     for i in range(lock_length, lock_length * 2):
#         for j in range(lock_length, lock_length * 2):
#             if new_lock[i][j] != 1:
#                 return False
#     return True


# def solution(key, lock):
#     n = len(lock)
#     m = len(key)

#     new_lock = [[0] * (n * 3) for _ in range(n * 3)]
#     for i in range(n):
#         for j in range(n):
#             new_lock[i + n][j + n] = lock[i][j]
    
#     for rotation in range(4):
#         key = rotate_a_metrix_by_90_degree(key)
#         for x in range(n * 2):
#             for y in range(n * 2):
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x + i][y + j] += key[i][j]
                
#                 if check(new_lock) == True:
#                     return True
                
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x + i][y + j] -= key[i][j]
#     return False

# print(solution(KEY, LOCK))


def rotate_a_metrix_90_degree(a):
    n = len(a)
    m = len(a[0])

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (3 * n) for _ in range(3 * n)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    
    for rotation in range(4):
        key = rotate_a_metrix_90_degree(key)

        for x in range(2 * n):
            for y in range(2 * n):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                
                if check(new_lock):
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    
    return False
            
