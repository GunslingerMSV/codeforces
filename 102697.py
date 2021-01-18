
"""
https://codeforces.com/gym/102697
CodeRams Practice Problem Archive
"""

def problem001() :
    """
    https://codeforces.com/gym/102697/problem/002
    полное решение))))
    """
    n = int(input())
    print(n ** 2)


def problem002() :
    """
    https://codeforces.com/gym/102697/problem/002
    полное решение
    """
    a = int(input())
    b = int(input())
    print(a * b * 3)


def problem003() :
    """
    https://codeforces.com/gym/102697/problem/003
    полное решение
    """
    n = int(input())
    res = 0
    for i in range(n) :
        a = int(input())
        res += a
    print(res * 3)


def problem004() :
    """
    https://codeforces.com/gym/102697/problem/004
    полное решение
    """
    n = int(input())
    T = [0] * n
    for i in range(n) :
        T[i] = int(input())
    for t in T :
        print((t - 2) * 180)


def problem005() :
    """
    https://codeforces.com/gym/102697/problem/005
    полное решение
    """
    n = int(input())
    if n % 3 == 0 : print("Fizz", end='')
    if n % 5 == 0 : print("Buzz", end='')
    print()


def problem006() :
    """
    https://codeforces.com/gym/102697/problem/006
    полное решение
    """
    a = [0] * 4
    for i in range(4) :
        a[i] = int(input())
    print(((a[0] - a[2]) ** 2 + (a[1] - a[3]) ** 2) ** 0.5)


def problem007() :
    """
    https://codeforces.com/gym/102697/problem/007
    полное решение
    """
    h = int(input())
    m = int(input())
    s = int(input())
    dp = input()
    if dp == "PM" : h += 12
    print((h * 60 + m) * 60 + s)


def problem008() :
    """
    https://codeforces.com/gym/102697/problem/008
    полное решение
    """
    n = int(input())
    res = 0
    for i in range(n) :
        a = int(input())
        b = int(input())    
        res += (a - b) ** 2
    print(res ** 0.5)


def problem009() :
    """
    https://codeforces.com/gym/102697/problem/009
    полное решение )))
    """
    print("Hello CodeRams")


def problem010() :
    """
    https://codeforces.com/gym/102697/problem/010
    полное решение
    """
    a = int(input())
    b = int(input())
    print(a / b)


def problem011() :
    """
    https://codeforces.com/gym/102697/problem/011
    полное решение
    """
    A = [int(el) for el in input().split()]
    res = 0
    for a in A : res += a
    print(res)


def problem012() :
    """
    https://codeforces.com/gym/102697/problem/012
    полное решение
    """
    n, k = (int(el) for el in input().split())
    print(n ** k)


def problem013() :
    """
    https://codeforces.com/gym/102697/problem/013
    полное решение
    """
    a = int(input())
    b = int(input())
    print(a * b / (a + b))


def problem014() :
    """
    https://codeforces.com/gym/102697/problem/014
    """
    n, m = (int(el) for el in input().split())
    s = [''] * n
    for i in range(n) :
        s[i] = input()
    cnt = 0
    for i in range(n) :
        for j in range(m) :
            if s[i][j] == 'x' : cnt += 1
    print(cnt)


def problem015() :
    """
    https://codeforces.com/gym/102697/problem/015
    Неверный ответ на тесте 3
    """       
    
    def findNextStation(aLines, aStation):
        import copy
        res = []
        arr = copy.deepcopy(aLines)
        for i in range(len(aLines)) :
            while True : # из этого цикла мы выйдем через exception
                try :
                    j = arr[i].index(aStation)
                    arr[i][j] = ''
                    if j < len(aLines[i]) - 1 : res.append(arr[i][j + 1])
                    if j > 0 : res.append(arr[i][j - 1])
                except :
                    break                
        return res


    n = int(input())
    lines = [0] * n
    minRoute = 0
    for i in range(n) :
        lines[i] = [el for el in input().split()]
        minRoute += len(lines[i])
    
    #n = 4
    #lines =[['Airport', 'CityCenter', 'WestStation'], ['CityCenter', 'Library', 'EastStation'], ['WestStation', 'Countryside'], ['Countryside', 'Library', 'Hotel']]
    #minRoute = 11

    path = [['Airport']]
    r = c = 0

    while True :
        if path[r][c] == 'Hotel' : 
            pass #minRoute = min(minRoute, len(path[r]))
        else :
            nextStations = findNextStation(lines, path[r][c])
            for station in nextStations :
                if station in path[r] : continue # на этой станции мы уже были
                elif c == len(path[r]) - 1 : path[r].append(station) # продолжаем движение на следующую станцию
                else : # создаем новый маршрут
                    path.append(path[r][0 : len(path[r]) - 1])
                    path[len(path) - 1].append(station)
                if station == 'Hotel' : break
        c += 1
        if c == len(path[r]) :
            r += 1
            if r == len(path) : break
            c = len(path[r]) - 1
        
    for i in range(len(path)) :
        if path[i][len(path[i]) - 1] == 'Hotel' :
            minRoute = min(minRoute, len(path[i]))
    print(minRoute - 1)
    
    

def problem016() :
    """
    https://codeforces.com/gym/102697/problem/016
    полное решение
    """   
    planet = input()
    if planet == 'EARTH' : print(9.807)
    elif planet == 'MARS' : print(3.711)


def problem017() :
    """
    https://codeforces.com/gym/102697/problem/017
    полное решение
    """
    a, b = (int(el) for el in input().split())
    print(b, a)


def problem018() :
    """
    https://codeforces.com/gym/102697/problem/018
    полное решение
    """
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n) : a[i], b[i] = (int(el) for el in input().split())    
    for i in range(n) : print(a[i] / b[i])


def problem019() :
    """
    https://codeforces.com/gym/102697/problem/019
    полное решение
    """
    n, m = (int(el) for el in input().split())
    b = [int(el) for el in input().split()]

    cnt = 0
    for i in range(n) :
        if m <= b[i] : cnt += 1
    print(cnt)


def problem020() :
    """
    https://codeforces.com/gym/102697/problem/021
    полное решение
    """
    n = int(input())
    s = [''] * n
    for i in range(n) :
        s[i] = input()

    for i in range(n) :
        for j in range(len(s[i])) :
            if j % 2 == 1 :
                s[i] = s[i][0 : j - 1] + s[i][j] + s[i][j - 1] + s[i][j + 1 : len(s[i])]
        print(s[i])


def problem021() :
    """
    https://codeforces.com/gym/102697/problem/021
    полное решение
    """
    n = int(input())
    m = int(input())
    print((n ** 2 - m ** 2) ** 0.5 + m)


def problem022() :
    """
    https://codeforces.com/gym/102697/problem/022
    полное решение
    """
    import math
    T1 = int(input())
    T2 = int(input())
    T3 = int(input())
    R1 = int(input())
    R2 = int(input())
    R3 = int(input())
    
    L1 = math.log(R1)
    L2 = math.log(R2)
    L3 = math.log(R3)
    Y1 = 1 / T1
    Y2 = 1 / T2
    Y3 = 1 / T3
    g2 = (Y2 - Y1) / (L2 - L1)
    g3 = (Y3 - Y1) / (L3 - L1)
    C = (g3 - g2) / (L3 - L2) / (L1 + L2 + L3)
    B = g2 - C * (L1 ** 2 + L1 * L2  + L2 ** 2)
    A = Y1 - L1 * (B + C * L1 ** 2)
                   
    print(A)


def problem023() :
    """
    https://codeforces.com/gym/102697/problem/023
    полное решение
    """
    v = float(input())
    print(v ** 2 / 2 / 9.8)


def problem024() :
    """
    https://codeforces.com/gym/102697/problem/024
    полное решение
    """
    name = [el for el in input().split()]
    point2 = [int(el) for el in input().split()]
    point3 = [int(el) for el in input().split()]
    point1 = [int(el) for el in input().split()]
    points = [0] * 2
    for i in range(2) : points[i] = point1[i] + point2[i] * 2 + point3[i] * 3
    print(name[points.index(max(points))])



def problem025() :
    """
    https://codeforces.com/gym/102697/problem/025
    полное решение
    """
    word = input()
    n = int(input())
    object = [''] * n
    for i in range(n) : object[i] = input()

    m = len(word)
    errors = [0] * n
    for i in range(n) :
        if len(object[i]) != m :
            errors[i] = m
            continue
        for j in range(m) :
            if word[j] != object[i][j] : errors[i] += 1
    print(object[errors.index(min(errors))])


def problem026() :
    """
    https://codeforces.com/gym/102697/problem/026
    полное решение
    """
    rules = input()

    print("Competition Rules:")
    print(rules)


def problem027() :
    """
    https://codeforces.com/gym/102697/problem/027
    полное решение
    """
    n = int(input())
    amount = 0
    for i in range(n) :
        payment = int(input())
        amount += payment
    print(amount)



def problem028() :
    """
    https://codeforces.com/gym/102697/problem/028
    полное рещение
    """
    n = int(input())
    if n % 5 == 0 and n % 7 == 0 : print("YES")
    else : print("NO")


def problem029() :
    """
    https://codeforces.com/gym/102697/problem/029
    полное решение
    """
    s = input()
    n = 0
    for i in range(len(s)) :
        if s[i] == 'o' : n += 1
    print(n)


def problem030() :
    """
    https://codeforces.com/gym/102697/problem/030
    полное решение
    """
    s = input()
    win = int(s[0 : s.index('-')])
    s = s[s.index('-') + 1 : len(s)]
    #loss = int(s[0 : s.index('-')])
    draw = int(s[s.index('-') + 1 : len(s)])
    print(win * 3 + draw)


def problem031() :
    """
    https://codeforces.com/gym/102697/problem/031
    """
    n = int(input())    
    if n % 2 == 0 : print(2)
    else : 
        for i in range(3, int(n ** 0.5) + 1, 2) :
            if n % i == 0:
                print(i)
                break


def problem032() :
    """
    https://codeforces.com/gym/102697/problem/032
    полное решение
    """
    n = int(input())
    res = 1
    for i in range(n) :
        a, b = (int(el) for el in input().split())
        res *= (abs(a - b) + 1)        
    print(res)


def problem033() :
    """
    https://codeforces.com/gym/102697/problem/033
    полное решение
    """
    n = int(input())
    made = attempte = 0
    for i in range(n) :
        m, a = (int(el) for el in input().split())
        made += m
        attempte += a
    print(round(made / attempte * 100, 2))

def problem034() :
    """
    https://codeforces.com/gym/102697/problem/034
    """
    n, k = (int(el) for el in input().split())
    ladder = [int(el) for el in input().split()]
    for i in range(1, n) :
        if ladder[i] - ladder[i - 1] > k :
            print("NO")
            return
    print("YES")


def problem035() :
    """
    https://codeforces.com/gym/102697/problem/035
    """
    n = int(input())
    arr = [int(el) for el in input().split()]

    cnt = 0
    st = set(arr)
    for el in st : cnt += 1
    print(cnt)

def problem036() :
    """
    https://codeforces.com/gym/102697/problem/036
    """    
    n = int(input())
    s = ['', 0]
    S = {}
    for i in range(n):
        s[0], s[1] = input().split()
        s[1] = int(s[1])
        S[s[0]] = s[1]    
    t = int(input())
    T = []
    for i in range(t):
        T.append(input())
    for t in T:
        print(S[t])

def problem037() :
    def gcd(a, b):
        if b == 0 :
            return a
        else:
            return gcd(b, a % b)
    
    """
    https://codeforces.com/gym/102697/problem/037
    """
    a, b = (int(el) for el in input().split())
    print(a * b // gcd(a, b))
    
    
def problem038() :
    """
    https://codeforces.com/gym/102697/problem/038
    """
    n = int(input())
    deck = [el for el in input().split()]    
    deckTotal = []
    for i in range(12) :
        s = i + 2
        if s == 1:
            s = 'A'
        elif s == 11 :
            s = 'J'
        elif s == 12 :
            s = 'Q'
        elif s == 13 :
            s = 'K'
        else : 
            s = str(s)
        deckTotal.append(s + 'C')
        deckTotal.append(s + 'D')
        deckTotal.append(s + 'H')
        deckTotal.append(s + 'S')
    deckTotal.append('AC')
    deckTotal.append('AD')
    deckTotal.append('AH')
    deckTotal.append('AS')
    deckSort = []    
    for card in deckTotal:        
        for i in range(n):
            if card == deck[i]:
                deckSort.append(card)                
                deck.remove(card)
                n-=1
                break
        if deck == [] :
            break
    s = ''
    for card in deckSort :
        s = s + ' ' + card
    s = s.strip()
    print(s)
    
def problem039() :
    """
    https://codeforces.com/gym/102697/problem/039
    """
    n = int(input())
    s = []
    for i in range(n) :
        s.append(input())
    for i in range(n) :
        s[i] = s[i].replace('0', 'o')
        s[i] = s[i].replace('1', 'i')
        s[i] = s[i].replace('3', 'e')
        s[i] = s[i].replace('4', 'a')
        s[i] = s[i].replace('5', 's')
        s[i] = s[i].replace('7', 't')
        print(s[i])
    
def problem040() :
    """
    https://codeforces.com/gym/102697/problem/040
    """
    sudoku = list()
    for i in range(9) :
        sudoku.append([int(el) for el in input().split()])
        
    for i in range(1, 10) : 
        for j in range(9) :
            #проверяем горизонтали
            c = 0
            for k in range(9) :
                if sudoku[j][k] == i :
                    c += 1
                    if c > 1 :
                        return 'INVALID'
            if c == 0 : 
                return 'INVALID'
            #проверяем вертикали
            c = 0
            for k in range(9) :
                if sudoku[k][j] == i :
                    c += 1
                    if c > 1 :
                        return 'INVALID'
            if c == 0 : 
                return 'INVALID'
        #проверяем сектора
        for j in range(3) :
            for k in range(3) :
                c = 0
                for l in range(3) :
                    for m in range(3) :
                        if sudoku[3 * j + l][3 * k + m] == i :
                            c += 1
                            if c > 1 :
                                return 'INVALID'
                if c == 0 :
                    return 'INVALID'
    return 'VALID'


def problem041() :
    """
    https://codeforces.com/gym/102697/problem/041
    """
    def sort041(lst):
        """
        сортировка списка результатов
        """
        b = True
        while b : # сортируем по очкам
            b = False
            for i in range(len(lst) - 1) :
                if lst[i][1] < lst[i + 1][1] :
                    lst[i][0], lst[i + 1][0] = lst[i + 1][0], lst[i + 1][0]
                    lst[i][1], lst[i + 1][1] = lst[i + 1][1], lst[i + 1][1]
                    b = True
        while b : # сортируем по названиям
            b = False
            for i in range(len(lst) - 1) :
                if lst[i][1] == lst[i + 1][1] and lst[i][0] < lst[i + 1][0]:
                    lst[i][0], lst[i + 1][0] = lst[i + 1][0], lst[i + 1][0]
                    lst[i][1], lst[i + 1][1] = lst[i + 1][1], lst[i + 1][1]
                    b = True
        return lst


    games = list()
    n = int(input())
    for i in range(n) :
        games.append([input().split()])
    #n = 6
    #games.append('Germany Portugal W'.split())
    #games.append('UnitedStates Ghana W'.split())
    #games.append('Germany Ghana T'.split())
    #games.append('UnitedStates Portugal T'.split())
    #games.append('Germany UnitedStates W'.split())
    #games.append('Portugal Ghana W'.split())
    
    teams = list()
    for i in range(n) :
        if not games[i][0] in teams :
            teams.append(games[i][0])
        if not games[i][1] in teams :
            teams.append(games[i][1])
    
    result = {}    
    for team in teams:
        result[team] = 0
    for game in games :
        if game[2] == 'W' :
            result[game[0]] += 3
        else :
            result[game[0]] += 1
            result[game[1]] += 1
    
    finalResult = list()
    for team in teams :
        finalResult.append([team, result[team]])
    finalResult = sort041(finalResult)
       
    for res in finalResult:
        print(res[0], res[1])
    

def problem() :
    """
    https://codeforces.com/gym/102697/problem/
    """

if __name__ == "__main__" :
    problem041()
    # 015 - неверный ответ на тесте 3