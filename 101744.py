"""
II Simulado Ingressantes
https://codeforces.com/gym/101744
"""

def ProblemA():
    """
    https://codeforces.com/gym/101744/problem/A
    полное решение
    """
    t = int(input())
    P = [[]] * t
    for i in range(t):
        P[i] = [int(el) for el in input().split()]    
    for i in range(t):        
        a = P[i][0]
        b = P[i][1]
        while True:
            c = max(a, b)
            b = min(a, b)
            a = c
            c = a % b
            if c == 0:
                print('Sim')
                break
            elif c == 1:
                print('Nao')
                break
            else:
                a = c

def ProblemB():
    """
    https://codeforces.com/gym/101744/problem/B
    полное решение
    """
    n = int(input())
    a = [int(el) for el in input().split()]
    i = 0
    m = n
    while i < m:    
        if n == 3:
            i += 2
            break
        elif n == 2:
            i += 2
            break
        elif n == 1:
            i += 1
            break
        else:
            i += 1             
            n //= 2                
    print(i)


def ProblemE():
    """
    https://codeforces.com/gym/101744/problem/E    
    полное решение
    """
    n, m = (int(el) for el in input().split())
    a =  [int(el) % 2 for el in input().split()]
    a.insert(0, 0)    
    
    for i in range(1, n + 1):
        a[i] += a[i - 1] 
    
    Res = [0] * m
    
    for i in range(m):
        l, r = (int(el) for el in input().split())            
        Res[i] = a[r] - a[l - 1]
    
    for i in range(m):
        if Res[i] % 2 == 0:
            print('Sim')
        else:
            print('Nao')        


def ProblemG():
    """
    https://codeforces.com/gym/101744/problem/G
    полное решение
    """
    s = input()
    j = 0
    for i in range(len(s)):
        if s[i] == 'A':
            j += 1
        else:
            j -= 1
        if j < 0:
            break
    if j == 0:
        print('Sim')
    else:
        print('Nao')

def ProblemH():
    """
    https://codeforces.com/gym/101744/problem/H
    полное решение
    """
    n = int(input())
    a = [int(el) for el in input().split()]
    b = [int(el) for el in input().split()]
    c = [int(el) for el in input().split()]
   
    ab = ac = 0
    for i in range(n):
        ab += ((a[i] - b[i]) ** 2)
        ac += ((a[i] - c[i]) ** 2)
    if ab <= ac:
        print('Yan')
    else:
        print('MaratonIME')

def ProblemI():
    """
    https://codeforces.com/gym/101744/problem/I
    полное решение
    """
    n, t = (int(el) for el in input().split())
    a = [int(el) for el in input().split()]
    
    Y = N = 0
    tY = tN = t
    for i in range(n):
        if tY >= a[i]:
            Y += 1
            tY -= a[i]
        else:
            break
    for i in range(n):        
        if tN >= a[-(i + 1)]:
            N += 1
            tN -= a[-(i + 1)]
        else:
            break    
    if Y > N:
        print('Yan')
    elif Y < N:
        print('Nathan')
    else:
        print('Empate')

def ProblemJ():
    """
    https://codeforces.com/gym/101744/problem/J
    """
    n = int(input())
    a = [[]] * n
    for i in range(n):
        a[i] = [int(el) for el in input().split()]

    for i in range(n):
        for j in range(i + 1, n):
            if (a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2 == (a[i][2] + a[j][2]) ** 2:
                print(i + 1, j + 1)

def ProblemK():
    """
    https://codeforces.com/gym/101744/problem/K
    полное решение
    """
    s = input()    
    n = len(s)
    Res = ''
    if n == 0:
        print(Res)
        return
    elif n == 1:
        Res = s + '1'
        print(Res)
        return
    else:
        C = s[0]
        j = 1
        for i in range(1, n):
            if s[i] == C:
                j += 1
            else:
                Res += (C + str(j))
                C = s[i]
                j = 1
        Res += (C + str(j))
        print(Res)
        return

def ProblemL():
    """
    https://codeforces.com/gym/101744/problem/L
    """
    N = int(input())
    h = [int(el) for el in input().split()]
    m = max(h)
    j = h.count(m)
    if j > 1:
        print(-1)
        return
    else:
        j = h.index(m)
        print(j + 1)
        return           

def ProblemM():
    """
    https://codeforces.com/gym/101744/problem/M    
    полное решение
    но надо признать, что я болван и мне подсказали что не факт что все монеты собранные до встречи с первым грабителем - искомое число, и возможно после грабителя монет будет больше
    """
    n, m = (int(el) for el in input().split())
    S = [''] * n
    for i in range(n):
        S[i] = input()

    c = cMax = 0       
    for i in range(n):
        if i % 2 == 0:
            for j in range(m):
                if S[i][j] == '.':
                    c += 1
                if S[i][j] == 'L':
                    if c > cMax:
                        cMax = c
                    c = 0
        else:
            for j in range(m - 1, -1, -1):
                if S[i][j] == '.':
                    c += 1
                if S[i][j] == 'L':
                    if c > cMax:
                        cMax = c
                    c = 0
    c = max(c, cMax)
    print(c)

def ProblemF():
    """
    https://codeforces.com/gym/101744/problem/F
    полное решение
    """
    n, m, k = (int(el) for el in input().split())
    if n == 0:
        print(0)
        print(100)
    x = n * 0.7
    if int(x) < x:
        x = int(x) + 1
    else:
        x = int(x)
    x -= k
    if x < 0:
        x = 0
    elif x > n - m:
        x = -1
    print(x)

    y = int((k + n - m) / n * 100)
    print(y)

def ProblemC():
    """
    https://codeforces.com/gym/101744/problem/C
    полное решение
    """
    x, y = (int(el) for el in input().split())
   
    while not (x == 0 and y == 0):
        
        if x == 0:
            print(2, y, flush=True)
            y = 0
            break
        elif y == 0:
            print(1, x, flush=True)
            x = 0
            break
        elif x == y:
            print(1, 1, flush=True)
            x -= 1
        elif x > y:
            print(1, x - y, flush=True)
            x = y
        elif y > x:
            print(2, y - x, flush=True)
            y = x

        if x == 0 and y == 0:
            break
        a, b = (int(el) for el in input().split())
        
        if a == 1:
            x -= b
        elif a == 2:
            y -= b  

        if x == 0 and y == 0:
            print('Lose!')
            break

def ProblemD():
    n = 8 #столько строк/столбцов у шахматной доски
    CB = [''] * n #ChessBoard
    for i in range(n):
        CB[i] = input()
    T = input() #Turn
    
    #CB = [ 'c.c..R..'
    #      ,'........'
    #      ,'.......b'
    #      ,'........'
    #      ,'........'
    #      ,'.......r'
    #      ,'........'
    #      ,'......r.' ]
    #T = 'f8'
    
    #p - pawn - пешка
    #t - tower - ладья
    #c - knight - конь
    #b - bishop - слон
    #r - queen - ферзь
    #k - king - король
    
    T = [abs(int(T[1]) - n), ord(T[0]) - ord('a')]   
    
    #пешка
    if T[0] < n - 1: # пешка д.б. на одну строку ниже слева иили справа от фигуры, пешка также не может стоять на последней линии
        if T[1] > 0 and CB[T[0] + 1][T[1] - 1] == 'p': #проверяем на пешку слева
            print('Sim')
            return
        if T[1] < n - 1  and CB[T[0] + 1][T[1] + 1] == 'p': #проверяем на пешку справа
            print('Sim')
            return

    #ладья и ферзь 
    for i in range(T[1] - 1, -1, -1): #ищем слева
        if CB[T[0]][i] == '.': #пустая клетка, ищем дальше
            continue
        elif CB[T[0]][i] in {'t', 'r'}: #нашли 
            print('Sim')
            return
        else: #какая-то другая фигура стоит на пути, выходим
            break

    for i in range(T[1] + 1, n): #ищем справа
        if CB[T[0]][i] == '.': #пустая клетка, ищем дальше
            continue
        elif CB[T[0]][i] in {'t', 'r'}: #нашли 
            print('Sim')
            return
        else: #какая-то другая фигура стоит на пути, выходим
            break

    for i in range(T[0] - 1, -1, -1): #ищем сверху
        if CB[i][T[1]] == '.': #пустая клетка, ищем дальше
            continue
        elif CB[i][T[1]] in {'t', 'r'}: #нашли 
            print('Sim')
            return
        else: #какая-то другая фигура стоит на пути, выходим
            break

    for i in range(T[0] + 1, n): #ищем снизу
        if CB[i][T[1]] == '.': #пустая клетка, ищем дальше
            continue
        elif CB[i][T[1]] in {'t', 'r'}: #нашли 
            print('Sim')
            return
        else: #какая-то другая фигура стоит на пути, выходим
            break
    
    #слон и ферзь
    #вверх-влево
    x = T[0]
    y = T[1]
    while True:
        x -= 1
        y -= 1
        if x < 0 or y < 0: #вышли за пределы доски
            break
        elif CB[x][y] == '.': #пустая клетка
            continue
        elif CB[x][y] in {'b', 'r'}: #нашли
            print('Sim')
            return
        else: #какая-то другая фигура
            break

    #вверх-вправо
    x = T[0]
    y = T[1]
    while True:
        x -= 1
        y += 1
        if x < 0 or y > n - 1: #вышли за пределы доски
            break
        elif CB[x][y] == '.': #пустая клетка
            continue
        elif CB[x][y] in {'b', 'r'}: #нашли
            print('Sim')
            return
        else: #какая-то другая фигура
            break

    #вниз-влево
    x = T[0]
    y = T[1]
    while True:
        x += 1
        y -= 1
        if x > n - 1 or y < 0: #вышли за пределы доски
            break
        elif CB[x][y] == '.': #пустая клетка
            continue
        elif CB[x][y] in {'b', 'r'}: #нашли
            print('Sim')
            return
        else: #какая-то другая фигура
            break

    #вниз-вправо
    x = T[0]
    y = T[1]
    while True:
        x += 1
        y += 1
        if x > n - 1 or y > n - 1: #вышли за пределы доски
            break
        elif CB[x][y] == '.': #пустая клетка
            continue
        elif CB[x][y] in {'b', 'r'}: #нашли
            print('Sim')
            return
        else: #какая-то другая фигура
            break

    #конь
    x = T[0]
    y = T[1]
    C = [[x - 1, y - 2], [x + 1, y - 2], [x - 2, y - 1], [x + 2, y - 1], [x - 2, y + 1], [x + 2, y + 1], [x - 1, y + 2], [x + 1, y + 2]] #точки в которых д.б. конь чтобы съесть
    for c in C:
        if c[0] < 0 or c[0] > n - 1 or c[1] < 0 or c[1] > n - 1: #вышли за пределы доски
            continue
        elif CB[c[0]][c[1]] == 'c': #нашли
            print('Sim')
            return
    #король
    #тут есть нюанс, с одной стороны король д.б. на любой смежной клетке, c другой стороны, между двумя королями д.б. минимум одна клетка. Но второе правило не отражено в условиях задачи
    K = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x + 1, y], [x + 1, y + 1], [x, y + 1], [x - 1, y + 1], [x - 1, y]]
    MaybeKing = False
    for k in K:
        if k[0] < 0 or k[0] > n -1 or k[1] < 0 or k[1] > n - 1: #вышли за пределы доски
            continue
        elif CB[k[0]][k[1]] == 'k': #нашли нашего короля
            MaybeKing = True
        #elif CB[k[0]][k[1]] == 'K': #нашли чужого короля, ход королем запрешен
        #    MaybeKing = False
        #    break
    if MaybeKing:
        print('Sim')
        return

    print('Nao')
    return

    
    



if __name__ == '__main__':
    ProblemD()