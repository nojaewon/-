words = list(input())
token = input()

stk = []
for word in words:
    stk.append(word)

    temp = ''.join(stk[-len(token):])
    if temp == token:
        for i in range(len(token)):
            stk.pop()

answer = ''.join(stk)
if answer:
    print(answer)
else:
    print('FRULA')

    
