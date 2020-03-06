"""
Amazalgo Uni 2019 Practice Contest 
https://codeforces.com/gym/102212
"""
def ProblemA():
    """
    https://codeforces.com/gym/102212/problem/A
    полное решение
    """
    a, b = (int(el) for el in input().split())
    print(a + b)

def ProblemB():
    """
    https://codeforces.com/gym/102212/problem/B
    полное решение
    """
    a, b = (int(el) for el in input().split())
    A = a
    B = b
    while True:
        if A == B:
            print(A)
            return
        elif A > B:
            B += b
        else:
            A += a

def ProblemC():
    """
    https://codeforces.com/gym/102212/problem/C
    полное решение
    """
    T = int(input())
    t = []
    for i in range(T):
        t.append(input().split())

    Res = []
    for i in range(T):
        Res.append('')
        for j in range(len(t[i])):
            s = t[i][j]
            if s.istitle():
                s = s.lower();
                s = s[1:len(s)] + s[0]                
                s += 'ay'
                s = s.title()                
            else:
                s = s[1:len(s)] + s[0]                
                s += 'ay'
            Res[i] += s + ' '
        Res[i] = Res[i].rstrip()
    
    for i in range(T):
        print(Res[i])

if __name__ == "__main__":
    ProblemC()