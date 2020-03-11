"""
12-й открытый турнир по программированию в Абакане
https://codeforces.com/gym/102189
"""

def ProblemA():
    """
    https://codeforces.com/gym/102189/problem/A
    полное решение
    """
    a, b = (int(el) for el in input().split())
    x, y = (int(el) for el in input().split())

    print(a * x + b * y)

def ProblemC():
    """
    https://codeforces.com/gym/102189/problem/C
    полное решение
    """
    n = int(input())
    a = [int(el) for el in input().split()]
    b = [int(el) for el in input().split()]
    Inc = False
    Dec = False

    for i in range(n):
        if b[i] > a[i]:
            Inc = True
        elif b[i] < a[i]:
            Dec = True

    if Inc and Dec:
        print("Rescaled")
    elif Inc and not Dec:
        print("Increased")
    elif not Inc and Dec:
        print("Reduced")
    elif not Inc and not Dec:
        print("Unchanged")
    else:
        print("Imposible")

def ProblemE():
    n, k = (int(el) for el in input().split())    
    k = (k + 1) * 2 #число возможных подключений
    if k >= n:
        print(0)
        return
    else:
        print((n - k + 1) // 2)
        return



if __name__ == "__main__":
    ProblemE()