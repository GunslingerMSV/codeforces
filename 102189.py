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

def ProblemB():
    """
    https://codeforces.com/gym/102189/problem/B
    """
    Separator = '|'
    Space = '.'
    TitlePlace = 'Place'
    TitleName = 'Name'
    TitleScore = 'Score'
    
    n = int(input())    
    #n = 5
    DataArr = [0] * n        
    MaxNameLen = len(TitleName)
    MaxScore = 0
    
    for i in range(n):
        N, S = (el for el in input().split())
        DataArr[i] = [N, int(S), S]
    
    #DataArr = [['Second', 100, '500'], ['Third1', 200, '200'], ['Third2', 200, '200'], ['First', 1000, '1000'], ['Fourth', 24, '24']]
    
    for i in range(n):
        if MaxScore < DataArr[i][1]:
            MaxScore = DataArr[i][1]
        NameLen = len(DataArr[i][0])
        if NameLen > MaxNameLen:
            MaxNameLen = NameLen
    MaxScoreLen = max(len(str(MaxScore)), len(TitleScore))
    for i in range(n):
        ScoreLen = len(DataArr[i][2])
        if ScoreLen < MaxScoreLen:
            DataArr[i] = ('0' * (MaxScoreLen - ScoreLen)) + DataArr[i][2] + DataArr[i][0]
        else:
            DataArr[i] = DataArr[i][2] + DataArr[i][0]
    DataArr.sort()
    DataArr.reverse()

    i = 0
    Res = [] * n
    MaxPlaceLen = len(TitlePlace)
    while i < n:
        if i < n - 1:
            for j in range(i + 1, n) :
                if DataArr[i][:MaxScoreLen] == DataArr[j][:MaxScoreLen]:
                    continue
                else:
                    break      
        else:
            j = i + 1
        Place = str(i + 1)
        if j - i > 1:
            Place = Place + '-' + str(j)
        PlaceLen = len(Place)
        if MaxPlaceLen < PlaceLen:
            MaxPlaceLen = PlaceLen
        for k in range(i, j):
            Name = DataArr[k][MaxScoreLen : len(DataArr[k])]
            Score = str(int(DataArr[k][ : MaxScoreLen]))
            DataArr[k] = [Place, Name, Score]
        i = j        

    Place =  Space * (MaxPlaceLen - len(TitlePlace)) + TitlePlace
    Name = TitleName + Space * (MaxNameLen - len(TitleName))
    Score = TitleScore + Space * (MaxScoreLen - len(TitleScore))
    print('', Place, Name, Score, '', sep=Separator)
    for i in range(i):
       Place =  Space * (MaxPlaceLen - len(DataArr[i][0])) + DataArr[i][0]
       Name = DataArr[i][1] + Space * (MaxNameLen - len(DataArr[i][1]))
       Score = DataArr[i][2] + Space * (MaxScoreLen - len(DataArr[i][2]))
       print('', Place, Name, Score, '', sep=Separator)

    
    

if __name__ == "__main__":
    ProblemB()