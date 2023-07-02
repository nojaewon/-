import sys
input = sys.stdin.readline

N = int(input().rstrip())
A, B, C, D, E, F = map(int, input().split())

if N == 1:
    print(sum([A, B, C, D, E, F]) - max([A, B, C, D, E, F]))
else:


    three = min([
        A + C + E,
        E + C + F,
        E + F + D,
        A + E + D,
        B + C + F,
        B + F + D,
        B + A + D,
        B + A + C
    ])

    two = min([A+B, B+D, C+F, A+D, B+F, C+E, A+E, B+C, A+C, D+F, D+E, E+F])
    one = min([A, B, C, D, E, F])

    print(three*4 + two*((N-1)*4+(N-2)*4) + one*(4*(N-1)*(N-2) + (N-2)*(N-2)))

