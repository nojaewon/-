from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1
    total_friends = list(permutations(dist, len(dist)))

    for start in range(length):
        for friends in total_friends:
            count = 1
            position = weak[start] + friends[count-1]

            for idx in range(start, start + length):
                if position < weak[idx]:    
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[idx] + friends[count-1]
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1

    return answer