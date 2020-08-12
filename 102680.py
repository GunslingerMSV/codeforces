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
            





if __name__ == "__main__":
    problemC()

