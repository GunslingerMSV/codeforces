
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


def problem() :
    """
    https://codeforces.com/gym/102697/problem/
    """


def problem() :
    """
    https://codeforces.com/gym/102697/problem/
    """


if __name__ == "__main__" :
    problem023()
    # 015 - неверный ответ на тесте 3