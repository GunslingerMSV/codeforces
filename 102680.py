"""
Brookfield Computer Programming Challenge 1
https://codeforces.com/gym/102680
"""

def problemA():
    """
    https://codeforces.com/gym/102680/problem/A
    полное решение
    """
    n, f = (int(el) for el in input().split())
    print(n)

def problemB():
    """
    https://codeforces.com/gym/102680/problem/B
    полное решение
    """
    n = int(input())
    s1 = []
    s2 = []
    for i in range(n):
        s1.append(input())
        s2.append(input())
        s1[i] = s1[i].replace("I have a ", "")
        s2[i] = s2[i].replace("I have a ", "")
    
    for i in range(n):
        print("Uh! " + s2[i] + "-" + s1[i] + "!")

def problemC():
    """
    https://codeforces.com/gym/102680/problem/C
    полное решение
    """
    T = int(input())
    N = []
    S = []
    TT = []
    for i in range(T):
        n, s = (int(el) for el in input().split())
        N.append(n)
        S.append(s)
        TT.append([int(el) for el in input().split()])

    for i in range(T):
        n = N[i]
        s = S[i]
        t = TT[i]        
        t.sort()
        flag = True
        for j in range(n - 1):            
            if t[j] + s > t[j + 1]:
                flag = False
                break
        if flag:
            print("NO")
        else:
            print("YES")
            
def problemD():
    """
    https://codeforces.com/gym/102680/problem/D
    полное решение
    """
    def isPrime(n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n

    n = int(input())
    q = []
    answer = ""
    for i in range(n):
        q.append(int(input()))

    for i in range(n):
        if q[i] == 1:
            answer = "Neither"
        else:
            answer = "Prime"
            if not isPrime(q[i]):
                answer = "Composite"                
        print(answer)

def problemE():
    """
    https://codeforces.com/gym/102680/problem/E
    полное решение
    """
    T = int(input())
    q = [0] * T
    n = [0] * T
    for i in range(T):
        q[i], n[i] = (int(el) for el in input().split())
    for i in range(T):
        j = 1
        N = 0
        while True:
            if q[i] > n[i] ** j:
                N += (n[i] ** j) * j
                q[i] -= n[i] ** j
            else:
                N += q[i] * j
                break
            j += 1
        print(N)
                
def problemF():
    """
    https://codeforces.com/gym/102680/problem/F
    полное решение
    """
    n, U = (int(el) for el in input().split())
    u = [0] * U
    for i in range(U):
        u[i] = [int(el) for el in input().split()]

    res = [[1, n]]
    
    for i in range(U):
        for j in range(len(res)):
            if u[i][1] < res[j][0]:                                                     # ( ) [ ] ->     [ ]
                pass
            elif u[i][0] < res[j][0] and u[i][1] >= res[j][0] and u[i][1] <= res[j][1]: # ( [ )  ] ->      [ ]
                res[j][0] = u[i][1] + 1
            elif res[j][0] <= u[i][0] and res[j][1] >= u[i][1]:                         # [  ( )  ] -> [ ]   [ ]
                if u[i][1] + 1 <= res[j][1]:
                    res.insert(j + 1, [u[i][1] + 1, res[j][1]])
                res[j][1] = u[i][0] - 1
            elif res[j][0] <= u[i][0] and res[j][1] >= u[i][0] and res[j][1] < u[i][1]: # [  ( ] ) -> [ ]
                res[j][1] = u[i][0] - 1                
            elif u[i][0] > res[j][1]:                                                   # [ ] ( ) -> [ ]
                pass
            
            if res[j][0] > res[j][1]:
                res[j] = [0, 0]
    
    for i in range(len(res)):
        if res[i] == [0, 0]:
            continue
        print(res[i][0])
        break

def problemG():
    """
    https://codeforces.com/gym/102680/problem/G
    """
    t = int(input())
    n = []
    m = []
    for i in range(t):
        n.append(0)
        m.append(0)
        n[i], m[i] = (int(el) for el in input().split())
#        for j in range(m[i]):

def problemH():
    """
    https://codeforces.com/gym/102680/problem/H
    полное решение
    """
    t = int(input())
    T = [0] *t
    for i in range(t):
        T[i] = int(input())
    
    

    s = [True]
    for i in range(t):
        a = 1
        j = 0
        while a < T[i]:
            a *= 2
        while a != 1:
            if a // 2 < T[i]:
                T[i] -= (a //2)
                a //= 2
                j += 1
            else:
                a //= 2
        if j % 2 == 0:
            print("Red")
        else:
            print("Blue")



if __name__ == "__main__":
    problemH()
    

