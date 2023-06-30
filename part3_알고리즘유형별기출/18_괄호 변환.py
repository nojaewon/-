P = '()))((()'

# ord('(') + ord(')') = 81
def is_balanced(s):
    total = 0
    for i in range(len(s)):
        total += ord(s[i])
    return total % 81 == 0

def is_right(s):
    if s[0] == ')': return False
    elif s[0] == '(': return True
    
def dfs(u, v=''):
    if u == '': return u
    for i in range(2, len(u), 2):
        if is_balanced(u[:i]):
            u, v = u[:i], u[i:] if i < len(u)-1 else ''
            break
    if is_right(u): return u + dfs(v)
    else: return f'({dfs(v)})' + ''.join(list(map(lambda x:'(' if x==')' else ')', u[1:-1]) ))
def solution(p):
    return dfs(p)



solution(P)
    
    

