
"""
https://codeforces.com/gym/102397
"""

def ProblemA():
    """
    https://codeforces.com/gym/102397/problem/A
    решена
    """
    x = int(input())
    Price = 2
    Cost = x * Price
    print(Cost)

def ProblemB():
    """
    https://codeforces.com/gym/102397/submit/B
    усложним себе задачу, так как понятно, что для того чтобы определить стороны прямоугольника площадью N достаточно вывести [1, N]
    Поэтому буду искать максимальный множитель меньше N/2
    решена
    """
    N = int(input())
    Width = int(N / 2)
    while Width > 1:        
        Width -= 1
        if N % Width == 0:
            Height = min(Width, N // Width)
            Width = N // Height
            print(Height, Width)
            return
    print(1, N)
    return

def ProblemC():
    """
    https://codeforces.com/gym/102397/problem/C
    решена
    """
    x, y = (int(el) for el in input().split())
    Path = input()    
    for i in range(len(Path)):        
        if Path[i] == "U":
            y += 1
        elif Path[i] == "D":
            y -= 1
        elif Path[i] == "L":
            x -= 1
        elif Path[i] == "R":
            x += 1
        else:
            print(Path[i], "Неверные исходные данные!")
            return
    print(x, y)

def ProblemDE():
    """
    https://codeforces.com/gym/102397/problem/D
    https://codeforces.com/gym/102397/problem/E
    задача D - полностью решена
    задача E - полностью решена
    """
    n, x = (int(el) for el in input().split())
    A = [int(el) for el in input().split()]
    
    if max(A) >= x:
        print(1)
        return
    Result = n
    Coins = 0
    for i in range(n):
        Coins += A[i]
    if Coins < x:
        print(-1)
        return
    elif Coins == x:
        print(Result)
        return
    else:
        for i in range(n - 1, 0, -1):
            Coins -= A[i]
            if Coins < x:
                Coins += A[i]
                Result = i + 1
                break  
    for i in range(1, n):
        Coins += (A[min(n - 1, i + Result - 1)] - A[i - 1])
        if Coins < x:
            continue
        for j in range(min(n - 1, Result + i - 1), i, -1):
            Coins -= A[j]
            if Coins < x:
                Coins += A[j]
                break
        if j < Result + i - 1:
            Result = j - i + 1
            if Result == 2:
                print(Result)
                return
    print(Result)

def ProblemF():
    """
    https://codeforces.com/gym/102397/problem/F
    решена
    """
    n = int(input())
    if n % 2 == 0:
        print('Mahmoud')
    else:
        print('Bashar')

def ProblemI():
    """
    https://codeforces.com/gym/102397/problem/I
    полное решение
    """
    n = int(input())
    s = input()
    An = Bn = Cn = Dn = En = 0
    for i in range(len(s)):
        if s[i] == 'a':
            An += 1
        elif s[i] == 'b':
            Bn += 1
        elif s[i] == 'c':
            Cn += 1
        elif s[i] == 'd':
            Dn += 1
        else:
            En += 1;
    print(min(An, Bn, Cn, Dn, En), max(An, Bn, Cn, Dn, En))

def ProblemJ():
    """
    https://codeforces.com/gym/102397/problem/J
    полное решение
    """
    n, x, a = (int(el) for el in input().split())
    Capacity = a // x
    Count = n // Capacity
    if n % Capacity != 0:
        Count += 1
    print(Count)

def ProblemH():    
    """
    https://codeforces.com/gym/102397/problem/H
    полное решение
    """
    n = int(input())
    a = [int(el) for el in input().split()]

    Flags = dict()
    for f in a:
        if f in Flags:
            Flags[f] += 1
        else:
            Flags.update({f : 1})
    Result = 0
    for i in Flags.values():
        Result += 2 ** i - 1
    Result %= 1000000007
    print(Result)
    return


def ProblemG():
    """
    https://codeforces.com/gym/102397/problem/G      
    првышено время выполнения на 19м тесте
    """

    def ListProcessing(List, N, Num):
        """
        метод выполняемый в рамках решение задачи G
        """
        n = N    
        Res = 0

        # для начала проверим есть ли в массиве элемент Num/2
        if Num // 2 == Num / 2:
            a = Num // 2
            i = 0
            Na = 0
            while i < n:
                if List[i] == a:
                    List.pop(i)
                    Na += 1
                    n -= 1
                    continue
                i += 1
            if Na > 1:
                for i in range(Na):
                    Res += i
        while n > 1:
            a = List.pop(0)
            n -= 1
            if a >= Num:
                i = 0
                while i < n:
                    if List[i] == a:
                        List.pop(i)
                        n -= 1
                        continue
                    i += 1
                continue
        
            i = 0
            b = Num - a
            Na = 1
            Nb = 0
            while i < n:
                if List[i] == a:
                    Na += 1
                    List.pop(i)
                    Res += Nb
                    n -= 1
                    continue
                if List[i] == b:
                    Nb += 1
                    List.pop(i)
                    Res += Na
                    n -= 1
                    continue
                i += 1
        return Res

    n, k = (int(el) for el in input().split())
    m = [int(el) for el in input().split()]
    b = [int(el) for el in input().split()]
    
    M = ListProcessing(m, n, k)
    B = ListProcessing(b, n, k)
    
    
    if M == B:
        print('Draw')
    elif M > B:
        print('Mahmoud')
    else:
        print('Bashar')
    return


"""
тело программы
"""
if __name__ == "__main__":
    ProblemG()    

    
