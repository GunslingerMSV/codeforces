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
    """
    https://codeforces.com/gym/102189/problem/E
    полное решение
    """
    n, k = (int(el) for el in input().split())    
    k = (k + 1) * 2 #число возможных подключений
    if k >= n:
        print(0)
        return
    else:
        print((n - k + 1) // 2)
        return

def ProblemB():
    """
    https://codeforces.com/gym/102189/problem/B
    так как почти на 2 недели забросил - не могу вернуться в старый код
    будем переделывать
    """
    Separator = '|'
    Space = '.'
    TitlePlace = 'Place'
    TitleName = 'Name'
    TitleScore = 'Score'
                    
    MaxNameLen = len(TitleName)
    MaxScore = 0
    MaxScoreLen = 0

    n = 5
    DataArr = [['Second', 100, '500', ''], ['Third1', 200, '200', ''], ['third2', 200, '200', ''], ['First', 1000, '1000', ''], ['Fourth', 24, '24', '']]
    
    #n = int(input())    
    #DataArr = [0] * n
    #for i in range(n):
    #    N, S = (el for el in input().split())
    #    DataArr[i] = [N, int(S), S, '']            
    for i in range(n):        
        ScoreLen = len(DataArr[i][2])
        if ScoreLen > MaxScoreLen:
            MaxScoreLen = ScoreLen
    
    for i in range(n):        
        DataArr[i][2] = '0' * (MaxScoreLen - len(DataArr[i][2])) + DataArr[i][2]
        DataArr[i][3] = DataArr[i][2] + DataArr[i][0].upper()
    
    print(DataArr)
    

if __name__ == "__main__":
    ProblemB()