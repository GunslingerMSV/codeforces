"""
2019-2020 ICPC Southwestern European Regional Programming Contest (SWERC 2019-20)
https://codeforces.com/gym/102501
"""

def ProblemA():    
    """
    https://codeforces.com/gym/102501/problem/A
    не решил - не правильный результат на тесте 5
 
    """
    def Dist(a, b):
        """
        Вычисляет расстояние между двумя точками
        """
        val = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
        if val > int(val):
            return int(val) + 1
        else:
            return int(val)
        

    #ввод исходных данных
    S = [int(el) for el in input().split()] #1 1
    D = [int(el) for el in input().split()] #10 2
    B = int(input()) #12
    CO0 = int(input()) #100
    T = int(input()) #2
    CO = [] #10\n50
    for i in range(T):
        CO.append(int(input()))    
    N = int(input()) #3
    L = [] #2 3 2 1 1 2 2\n5 5 1 2 1\n9 3 0
    for i in range(N): 
        Tmp = [int(el) for el in input().split()]
        L.append([])
        L[i].append([Tmp[0], Tmp[1]])        
        L[i].append(Tmp[2])        
        if Tmp[2] > 0:
            for j in range(0, Tmp[2], 1):
                L[i].append([Tmp[3 + 2 * j], Tmp[4 + 2 * j]])                
    # окончание ввода исходных данных

    #начало выполнения 
    
    #сконвертируем исходные данные в более удобную для обработки форму
    CO.insert(0, CO0) #массив данных о выхлопах транспорта дополним данными об автомобиле
    
    # перенумераем станции, так как в дальнейшем, мы будем считать, что станция с номером 0 - начало пути, а станция с номером (N + 1) - окончание
    for i in range(len(L)):
        if L[i][1] != 0:
            for j in range(2, 2 + L[i][1]):
                L[i][j][0] += 1
    
    # дополним массив L данными о точке старта и точке окончания
    L.insert(0, [S, N + 1])
    L.append([D, 0])
    for i in range(1, N + 2):
        val = [i, 0]
        L[0].append(val)
        L[i][1] += 1
        L[i].append([4, 0])
    L[N + 1].pop()
    L[N + 1][1] = 0
    #окончание конвертации
    
    #создадим массив возможных путей
    Path = []
    for i in range(1, N + 2):
        Path.append('0' + str(i))
    
    l = 0
    Flag = True
    while Flag:
        Flag = False
        k = l
        for i in range(k, len(Path)):
            if int(Path[i][len(Path[i]) - 1]) == N + 1: # этот путь уже полностью достроен
                continue                                # пропускаем итерацию
            l = i
            for j in range(1, N + 1):
                if Path[i].find(str(j)) == -1:
                    Path.append(Path[i] + str(j))                    
            Path[i] += str(N + 1)
            Flag = True
            break
    #окончание создания массива возможных путей

    #находим параметры возможных путей (расстояние и размера выхлопов)
    Res = []
    for i in range(len(Path)):        
        Res.append([0, 0])
        for j in range(0, len(Path[i]) - 1):
            Depart = int(Path[i][j])
            Dest = int(Path[i][j + 1])
            
            Flag = True
            #посмотрим связь между точками по станции отправления
            for k in range(2, L[Depart][1] + 2):
                if L[Depart][k][0] == Dest: # найден путь между точками
                    Flag = False
                    C = CO[L[Depart][k][1]]
                    break
            
            if Flag: # посмотрим связь между точками по станции назначения
                for k in range(2, L[Dest][1] + 2):
                    if L[Dest][k][0] == Depart: # найден путь между точками
                        Flag = False
                        C = CO[L[Dest][k][1]]
                        break

            if Flag: # между точками маршрута нет сообщения, маршрут непригоден
                Res[i][0] = -2
                Res[i][1] = -2
                break

            tmp = Dist(L[Depart][0], L[Dest][0])
            Res[i][0] += tmp            
            if Res[i][0] > B: # превышено требование на предельную длину маршрута, маршрут непригоден
                Res[i][0] = -1
                Res[i][1] = -1
                break       
            Res[i][1] += tmp * C

    val = -1
    for i in range(len(Path)):
        if Res[i][0] < 0:
            continue
        if val > Res[i][1] or val == -1:
            val = Res[i][1]

    print(val)
    return(val)

def ProblemB():
    """
    https://codeforces.com/gym/102501/problem/B
    полностью решил
    """
    
    # ввод данных - начало
    N = int(input())
    Arr = []
    for i in range(N):
        Arr.append(input())
    # ввод данных - завершение

    # решение - начало
    Dict = {} # занесем введеные данные в словарь
    for s in Arr:
        if s in Dict:
            Dict[s] += 1
        else:
            Dict.update({s : 1})
    print(Dict)
    # проанализируем данные в словаре
    Flag = True
    for key in Dict:
        if Dict[key] > N - Dict[key]:
            Flag = False
            print(key)
            break
    if Flag:
        print("NONE")

def ProblemC():
    """
    https://codeforces.com/gym/102501/problem/C
    не решил - превышено ограничение времени на тесте 10
    """
    
    N = int(input())   
    if N <= 0:
        print(0)
    else: 
        X = []
        for i in range(N):
            x = int(input())
            if x >= 0:
                X.append(x)
        X.sort()
        N = len(X)
        if N == 0:
            print(0)
            return
        elif X[0] > 0:
            print(0)
            return
        else:
            for i in range(1, N):
                if X[i] - X[i - 1] > 1:
                    print(X[i - 1] + 1)
                    return
            print(X[i] + 1)
            return

def ProblemI():
    """
    https://codeforces.com/gym/102501/problem/I
    полное решение
    """
    x1, x2, x12 = [int(el) for el in input().split()]    
    N = int((x1 + 1) * (x2 + 1) / (x12 + 1) - 1)
    print(N)


def ProblemF():
    """
    https://codeforces.com/gym/102501/problem/F
    задача не решена - неправильный результат на тесте 3, в принципе я понимал сразу что загвоздка с невыпуклыми многоугольниками, но не знал как решить ее, пошел по неправильному пути. 
    Правльный ответ я подсмотрел и знаю теперь как ее решать, но сдавать естественно не буду.
    """
    def GroundRectangularTapestryArea(A, B):
        """
        функция вычисляет площадь прямоугольной трапеции, одна боковая грань которой лежит на оси X
        То есть, если заданы две точки А = [x1, y1] и B = [x2, y2], то вычисляется площадь трапеции получаемой соединением точек A, B, B0 = [x2, 0], A0 = [x1, 0]
        """
        return abs((B[0] - A[0]) * (A[1] + B[1])) / 2

    #ввод данных - начало    
    N = int(input())
    P = []
    for i in range(N):        
        n = int(input())
        a = []
        for j in range(n):
            b = [int(el) for el in input().split()]
            a.append(b)
        a.insert(0, n)
        P.append(a)   
    #ввод данных - окончание    
    #решение            
    R = 0  
    for i in range(N):
        S = 0
        for j in range(1, P[i][0]):
            s = GroundRectangularTapestryArea(P[i][j], P[i][j + 1])
            if P[i][j][0] > P[i][j + 1][0]:
                s = -s
            S = S + s
        s = GroundRectangularTapestryArea(P[i][j + 1], P[i][1])
        if P[i][j + 1][0] > P[i][1][0]:
                s = -s
        S = S + s
        R = R + abs(S)
           

    #решение - окончания  
    print(int(R))


"""
тело программы
"""
if __name__ == "__main__":
    ProblemF()
    
