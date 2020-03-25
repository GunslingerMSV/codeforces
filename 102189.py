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
    буду переделывать
    """
    Separator = '|'
    Space = '.'
    TitlePlace = 'Place'
    TitleName = 'Name'
    TitleScore = 'Score'
                        
    #n = 6
    #DataArr = [['Second1', 500, '500', ''], ['Third', 200, '200', ''], ['fourth2', 24, '24', ''], ['First', 1000, '1000', ''], ['Fourth1', 24, '24', ''], ['Second2', 500, '500', '']]#, ['Fifth', 5, '5', '']]
    
    n = int(input())    
    DataArr = [0] * n
    for i in range(n):
        N, S = (el for el in input().split())
        DataArr[i] = [N, int(S), S, '']            
    
    MaxScoreLen = len(TitleScore)
    for i in range(n):        
        ScoreLen = len(DataArr[i][2])
        if ScoreLen > MaxScoreLen:
            MaxScoreLen = ScoreLen
    DataList = dict()
    for i in range(n):        
        DataArr[i][2] = '0' * (MaxScoreLen - len(DataArr[i][2])) + DataArr[i][2]
        DataArr[i][3] = DataArr[i][2] + DataArr[i][0].upper()
        DataList[DataArr[i][3]] = [DataArr[i][0], DataArr[i][1]] 
        DataArr[i] = DataArr[i][3]
    DataArr.sort()
    DataArr.reverse()
    
    i = 0
    Place = 1
    while i < n:
        for j in range(i, n):
            if DataList[DataArr[i]][1] == DataList[DataArr[j]][1]:
                continue
            j -= 1
            break                
        if i == j:
            DataArr[i] = [str(Place), DataList[DataArr[i]][0], str(DataList[DataArr[i]][1])]
            Place += 1
        else:
            strPlace = str(Place) + '-' + str(Place + j - i) 
            for k in range(i, j + 1):
                DataArr[k] = [strPlace, DataList[DataArr[k]][0], str(DataList[DataArr[k]][1])]
            Place += (j - i + 1)        
        i = j + 1
        
    MaxNameLen = len(TitleName)
    MaxPlaceLen = len(TitlePlace)
    for x in DataArr:
        PlaceLen = len(x[0])
        NameLen = len(x[1])
        if PlaceLen > MaxPlaceLen:
            MaxPlaceLen = PlaceLen
        if NameLen > MaxNameLen:
            MaxNameLen = NameLen
    
    Place =  Space * (MaxPlaceLen - len(TitlePlace)) + TitlePlace
    Name = TitleName + Space * (MaxNameLen - len(TitleName))
    Score = TitleScore + Space * (MaxScoreLen - len(TitleScore))
    print('', Place, Name, Score, '', sep=Separator)
    
    for x in DataArr:
        Place =  Space * (MaxPlaceLen - len(x[0])) + x[0]
        Name = x[1] + Space * (MaxNameLen - len(x[1]))
        Score = x[2] + Space * (MaxScoreLen - len(x[2]))
        print('', Place, Name, Score, '', sep=Separator)    
    
def Test():
    a = ['DZ', 'DX', 'DY']
    a.sort()
    print(a)

if __name__ == "__main__":
    Test()