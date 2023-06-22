def permutation(arr, r):
    # 1
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2
        if len(chosen) == r:
            print(chosen)
            return
        # 3:
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)

# permutation([1,2,3,4,5], 3)

def combination(arr, r):
    # 1
    arr = sorted(arr)

    # 2
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return
        
        # 3
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])