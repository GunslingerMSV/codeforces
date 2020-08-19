"""
12-й открытый турнир по программированию в Абакане
https://codeforces.com/gym/102189
"""

def problemA():
    """
    https://codeforces.com/gym/102189/problem/A
    полное решение
    """
    a, b = (int(el) for el in input().split())
    x, y = (int(el) for el in input().split())

    print(a * x + b * y)

def problemC():
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

def problemE():
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

def problemB():
    """
    https://codeforces.com/gym/102189/problem/B
    превышение лимита врамени на тесте 5. Проблема КМК в скорости сортировок массивов. буду переделывать
    """
    n = int(input())    
    name = [''] * n
    score = [0] * n
    place = [''] * n

    for i in range(n):
        name[i], score[i] = (el for el in input().split())
        score[i] = int(score[i])

    
    #name = ['Petr','tourist','Bredor','dZ','dx','Dy','pressF','user']
    #score = [100,100,9999,5,5,5,0,35]

    placeLen = 5
    nameLen = 4
    scoreLen = 5    
    placeTitle = 'Place'
    nameTitle = 'Name'
    scoreTitle = 'Score' 
    
    

    # занесем данные в словарь
    dictData = dict()
    for i in range(n):
        if score[i] in dictData:
            dictData[score[i]].append(name[i])
        else:
            dictData[score[i]] = [name[i]]

    sortScore = list(dictData.keys())
    sortScore.sort()
    sortScore.reverse()
    
    i = 0
    placeStr = ''
    for scoreKey in sortScore:
        dictData[scoreKey].sort(key=str.lower)
        if len(dictData[scoreKey]) == 1:
            placeStr = str(i + 1)
        else:
            placeStr = str(i + 1) + '-' + str(i + len(dictData[scoreKey]))
        for nameKey in dictData[scoreKey]:
            score[i] = str(scoreKey)
            if len(score[i]) > scoreLen : scoreLen = len(score[i])
            name[i] = nameKey
            if len(name[i]) > nameLen : nameLen = len(name[i])
            place[i] = placeStr
            if len(place[i]) > placeLen : placeLen = len(place[i])
            i += 1
    place.insert(0, placeTitle)
    name.insert(0, nameTitle)
    score.insert(0, scoreTitle)
    for i in range(n + 1):
        for j in range(placeLen - len(place[i])) : place[i] = '.' + place[i]
        place[i] = '|' + place[i]
        for j in range(nameLen - len(name[i])) : name[i] += '.'
        for j in range(scoreLen - len(score[i])) : score[i] += '.'
        score[i] += '|'

    
    for i in range(n + 1):
        print(place[i], name[i], score[i], sep='|')

def problemG():
    """
    https://codeforces.com/gym/102189/problem/G
    полное решение
    """
    a, b = (int(el) for el in input().split())
    p= [int(el) for el in input().split()]
    #a, b= 1, 1
    #p = [33, 33, 33, 1]

    x = y = 0
    for i in range(4) :
        for j in range(4) :
            if i == j : continue
            if 2 * p[i] == 100 - 2 * p[j]:
                for k in range(4) :
                    if k == i or k == j : continue
                    for l in range(4) :
                        if l == i or l == j : continue
                        if k == l : continue
                        if 2 * p[l] == 100 - 2 * p[k] :
                            x = 2 * p[i] * a / 100
                            y = 2 * p[k] * b / 100
                            break
    
    if x != 0 and y != 0 :
        print('YES')
        print(x)
        print(y)
    else:
        print('NO')

def problemD_1():
    """
    https://codeforces.com/gym/102189/problem/D
    решение брутфорсом- дает перерасход времени на тесте 23
    """
    n, m = (int(el) for el in input().split())
    func = [['', '', '']] * m
    for i in range(m):
        func[i] = [el for el in input().split()]
        func[i][1] = int(func[i][1])
        func[i][2] = int(func[i][2])
    pos = int(input())

    #n, m = 5, 4
    #func = [['', '', '']] * m
    #func[0] = ['inverse', 1, 3]
    #func[1] = ['reverse', 2, 5]
    #func[2] = ['reverse', 1, 3]
    #func[3] = ['inverse', 2, 4]
    #pos = 3

    d = [0] * (n + 1)
    for i in range(1, n + 1) :
        d[i] = i

    for i in range(m):
        if func[i][0] == 'inverse' :
            a = d[0 : func[i][1]]
            b = [-el for el in d[func[i][1] : func[i][2] + 1]]
            c = d[func[i][2] + 1 : len(d)]
            d = a + b + c
        elif func[i][0] == 'reverse' :
            a = d[0 : func[i][1]]
            b = d[func[i][1] : func[i][2] + 1]
            c = d[func[i][2] + 1 : len(d)]
            b.reverse();
            d = a + b + c
        
    print(d[pos])
    
def problemD():
    """
    https://codeforces.com/gym/102189/problem/D
    так как брутфорс просел по времени - попытаемся развернуть последовательность действий обратно и понять что с числом происходило
    полное решение
    """
    n, m = (int(el) for el in input().split())
    func = [['', '', '']] * m
    for i in range(m):
        func[i] = [el for el in input().split()]
        func[i][1] = int(func[i][1])
        func[i][2] = int(func[i][2])
    pos = int(input())
    
    mult = 1
    for i in range(m - 1, -1, -1):
        if func[i][1] <= pos and func[i][2] >= pos : #эта функция затрагивает наше число
            if func[i][0] == 'inverse' : mult *= (-1)
            else: pos = func[i][1] + func[i][2] - pos
    print(pos * mult)

def problemF():
    """
    https://codeforces.com/gym/102189/problem/F
    ошибка на 15м тесте
    """
    n = int(input())
    b = [int(el) for el in input().split()]
    #n = 10
    #b = [1, 1, 1,1,1,1,1,1,1,1]
    
    even = odd = 0
    for i in range(n) :
        if i % 2 == 0 : #четные
            even += b[i]
        else : #нечетные
            odd += b[i]
    
    a = [1] * (odd + even)
    k = -1

    if even >= odd :
        for i in range(n) :
            if i % 2 == 0 : k += b[i]               
            else: 
                for j in range(b[i]) :
                    k += 1
                    a[k] = 2
    else:
        for i in range(n) :
            if i % 2 == 1 : k += b[i]
            else :
                for j in range(b[i]) :
                    k += 1
                    a[k] = 2                
    
    for i in range(len(a)): print(a[i], end=' ')
    print()

if __name__ == "__main__":
    problemF()